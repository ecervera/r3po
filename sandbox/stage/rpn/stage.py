#!/usr/bin/env python

import rospy

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

def forward(v=1.0):
	twist = Twist()
	twist.linear.x = v
	cmd_vel_publisher.publish(vel)

def fd(v=1.0):
	forward(v)

def backward(v=1.0):
	forward(-v)

def bk(v=1.0):
	backward(v)
    
def turn(a=-90.0,t=1.0):
	vel.linear = 0.0
	vel.angular = math.radians(a)
	turtle_vel.publish(vel)
	sleep(t)
    
def right(a=90.0,t=1.0):
	turn(-a,t)

def rt(a=90.0,t=1.0):
	right(a,t)

def left(a=90.0,t=1.0):
	turn(a,t)

def lt(a=90.0,t=1.0):
	left(a,t)

def rightArc(a=90.0,r=1.0,t=1.0):
	vel.linear = math.radians(a) * r
	vel.angular = -math.radians(a)
	turtle_vel.publish(vel)
	sleep(t)
	
def leftArc(a=90.0,r=1.0,t=1.0):
	vel.linear = math.radians(a) * r
	vel.angular = math.radians(a)
	turtle_vel.publish(vel)
	sleep(t)
	
