#!/usr/bin/env python

import rospy, math

from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

def loginfo(s=''):
	rospy.loginfo(s)

def display(s=''):
	loginfo(s)

def sleep(t=1.0):
	rospy.sleep(t)

def callback_base_scan(data):
	global base_scan_ranges
	base_scan_ranges = data.ranges

def callback_odom(data):
	global odom_pose_pose_position, odom_pose_pose_orientation
	odom_pose_pose_position = data.pose.pose.position
	odom_pose_pose_orientation = data.pose.pose.orientation

def start():
	global cmd_vel_publisher
	rospy.init_node('stage_controller', anonymous=True)
	cmd_vel_publisher = rospy.Publisher('cmd_vel', Twist)
	rospy.Subscriber("base_scan", LaserScan, callback_base_scan)
	rospy.Subscriber("odom", Odometry, callback_odom)
	sleep(1.0)

def move(v=1.0,w=0.0):
	twist = Twist()
	twist.linear.x = v
	twist.angular.z = math.radians(w)
	cmd_vel_publisher.publish(twist)

def getPosition():
	return odom_pose_pose_position

def getRanges():
	return base_scan_ranges

BACK = 0
BACK_RIGHT = 1
RIGHT_BACK = 2
RIGHT = 3
RIGHT_FRONT = 4
FRONT_RIGHT = 5
FRONT = 6
FRONT_LEFT = 7
LEFT_FRONT = 8
LEFT = 9
LEFT_BACK = 10
BACK_LEFT = 11

def forward(v=1.0):
	move(v,0.0)

def fd(v=1.0):
	forward(v)

def backward(v=1.0):
	forward(-v)

def bk(v=1.0):
	backward(v)
    
def stop():
	forward(0.0)

def turn(w=-90.0):
	move(0.0,w)
    
def right(w=90.0):
	turn(-w)

def rt(w=90.0):
	right(w)

def left(w=90.0):
	turn(w)

def lt(w=90.0):
	left(w)

