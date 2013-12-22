#!/usr/bin/env python
import rospy

from std_msgs.msg import Empty
from turtlesim.msg import Pose

def callback(data):
	global pub
	bumper = Empty()
	#bumper.data = True
	if data.x > 11.08888:	
	    pub.publish(bumper)
	elif data.x == 0.0:
	    pub.publish(bumper)
	elif data.y > 11.08888:	
	    pub.publish(bumper)
	elif data.y == 0.0:
	    pub.publish(bumper)

def listener():
    rospy.init_node('turtle_monitor', anonymous=True)
    rospy.Subscriber("pose", Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    global pub
    pub = rospy.Publisher('bumper', Empty)
    listener()
