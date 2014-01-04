#!/usr/bin/env python

import rospy
from r3po.srv import *

def handle_acquire(req):
	global acquired
	avail = [stage for stage, isAcquired in acquired.iteritems() if not isAcquired]
	if len(avail)==0:
		available_stage = ''
	else:
		print avail
		available_stage = avail[0]	
		acquired[available_stage] = True
		print 'Acquired '+available_stage
	return AcquireResponse(available_stage)

def handle_release(req):
	global acquired
	if req.name in acquired:
		acquired[req.name] = False
		print 'Released '+req.name
	else:
		print 'Wrong key: '+req.name
	return 0

def stage_scheduler():
	global acquired
	rospy.init_node('stage_scheduler')
	sr = rospy.Service('~acquire', Acquire, handle_acquire)
	sp = rospy.Service('~release', Release, handle_release)
	acquired = {}
	acquired['stage1'] = False
	acquired['stage2'] = False
	acquired['stage3'] = False
	acquired['stage4'] = False
	print "Ready for requests."
	rospy.spin()

if __name__ == "__main__":
	stage_scheduler()
