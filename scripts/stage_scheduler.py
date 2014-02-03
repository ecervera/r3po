#!/usr/bin/env python

import rospy
from r3po.srv import *
import subprocess, os, signal, time

def terminate_process_and_children(p):
    ps_command = subprocess.Popen("ps -o pid --ppid %d --noheaders" % p.pid, shell=True, stdout=subprocess.PIPE)
    ps_output = ps_command.stdout.read()
    retcode = ps_command.wait()
    assert retcode == 0, "ps command returned %d" % retcode
    for pid_str in ps_output.split("\n")[:-1]:
            os.kill(int(pid_str), signal.SIGINT)
    p.terminate()

def handle_acquire(req):
	global stage_proc, pose_proc, number
	stage = 'stage'+str(number)
	number = number + 1
	world = req.world + '.world'
	my_env = os.environ
	my_env["ROS_NAMESPACE"] = stage
	stage_proc[stage] = subprocess.Popen('rosrun stage stageros -g $(rospack find r3po)/stage/' + world + ' /clock:=clock',
									env=my_env,
									shell=True)
	pose_proc[stage] = subprocess.Popen('rosrun r3po robot_pose.py',env=my_env,shell=True)
	subprocess.Popen('sleep 1; rosparam set /use_sim_time false',shell=True)
	return AcquireResponse(stage)

def handle_release(req):
	global stage_proc, pose_proc
	stage = req.name 
	terminate_process_and_children(stage_proc[stage])
	terminate_process_and_children(pose_proc[stage])
	return 0

def stage_scheduler():
	global stage_proc, pose_proc, number
	rospy.init_node('stage_scheduler')
	sr = rospy.Service('~acquire', Acquire, handle_acquire)
	sp = rospy.Service('~release', Release, handle_release)
	number = 1
	stage_proc = {}
	pose_proc = {}
	rospy.spin()

if __name__ == "__main__":
	stage_scheduler()
