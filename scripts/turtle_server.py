#!/usr/bin/env python
import roslib; roslib.load_manifest('r3po')

import rospy
import actionlib

from r3po.msg import RunScriptAction, RunScriptResult

import subprocess, os, signal, time

def terminate_process_and_children(p):
    ps_command = subprocess.Popen("ps -o pid --ppid %d --noheaders" % p.pid, shell=True, stdout=subprocess.PIPE)
    ps_output = ps_command.stdout.read()
    retcode = ps_command.wait()
    assert retcode == 0, "ps command returned %d" % retcode
    for pid_str in ps_output.split("\n")[:-1]:
            os.kill(int(pid_str), signal.SIGINT)
    p.terminate()
    
class TurtleServer:
  def __init__(self):
    self.server = actionlib.ActionServer('turtlesim_run_script', RunScriptAction, self.execute, self.cancel, False)
    self.goalHandle = {}
    self.goal = {}
    self.pm = {}
    self.cancelled = {}
    self.executing = {}
    self.filename = {}
    self.result = {}
    self.server.start()

  def cancel(self, goalHandle):
    goal = goalHandle.get_goal()
    turtle = goal.param
    self.cancelled[turtle] = True
    terminate_process_and_children(self.pm[turtle])
     
  def execute(self, goalHandle):
    goal = goalHandle.get_goal()
    turtle = goal.param
    self.goalHandle[turtle] = goalHandle
    self.goal[turtle] = goal
    modulename = goal.name + '_' + time.strftime("%Y%m%d_%H%M%S", time.gmtime())
    self.filename[turtle] = '/home/r3po/catkin_ws/src/r3po/sandbox/turtlesim/'+ modulename

    goalHandle.set_accepted()
    
    with open(self.filename[turtle]+'.py', "w") as text_file:
        text_file.write(goal.code)
    os.chmod(self.filename[turtle]+'.py', 0755)
            
    self.result[turtle] = RunScriptResult()
    self.result[turtle].name = modulename
    
    my_env = os.environ
    my_env["ROS_NAMESPACE"] = turtle
    with open(self.filename[turtle]+'.output', "w") as text_file:
        self.pm[turtle] = subprocess.Popen('rosrun r3po sandbox/turtlesim/' + modulename+'.py',
                                stdout=text_file,
                                stderr=subprocess.STDOUT,
                                env=my_env,
                                shell=True)
    self.cancelled[turtle] = False
    self.executing[turtle] = True
    
def poll(event):
  global server
  for turtle in server.executing:
    if server.executing[turtle]:
        if server.pm[turtle].poll() is None:
            pass
        else:
            server.executing[turtle] = False
            server.result[turtle].return_value = server.pm[turtle].returncode
            with open(server.filename[turtle]+'.output', "r") as text_file:
                server.result[turtle].output = text_file.read()
            if server.cancelled[turtle]:
                server.result[turtle].output += 'Aborted!\n'
                server.goalHandle[turtle].set_aborted(server.result[turtle])
            else:
                server.goalHandle[turtle].set_succeeded(server.result[turtle])

if __name__ == '__main__':
  global server
  rospy.init_node('turtle_server')
  rospy.loginfo("Starting turtle_server...")
  server = TurtleServer()
  rospy.Timer(rospy.Duration(0.2), poll)
  rospy.spin()
