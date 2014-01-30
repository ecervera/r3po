#!/usr/bin/env python

import rospy, math

from geometry_msgs.msg import Twist 

def sleep(t=1.0):
	rospy.sleep(t)

def start():
	global cmd_vel_publisher
	rospy.init_node('stage_controller', anonymous=True)
	cmd_vel_publisher = rospy.Publisher('cmd_vel', Twist)
	sleep(0.7)

def loginfo(s=''):
	rospy.loginfo(s)

def display(s=''):
	loginfo(s)

def move(v=1.0,w=0.0):
	twist = Twist()
	twist.linear.x = v
	twist.angular.z = math.radians(w)
	cmd_vel_publisher.publish(twist)

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

