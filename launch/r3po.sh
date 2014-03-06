#!/bin/bash

# Create 3x3 frames, with borders and 240px row height, to display six terminals
gframe -c 3 -b -r 240 -t rosbridge mjpeg_server turtlesim turtle_server turtle_recorder stage_nodes stage_server nao_server nao_driver nao_camera freezer_driver freezer_camera

sleep 5

gsh -c rosbridge gmenu view menubar on
gsh -c mjpeg_server gmenu view menubar on

gsh -c turtlesim gmenu view menubar on
gsh -c turtle_server gmenu view menubar on
gsh -c turtle_recorder gmenu view menubar on

gsh -c stage_server gmenu view menubar on
gsh -c stage_nodes gmenu view menubar on

gsh -c nao_server gmenu view menubar on
gsh -c nao_driver gmenu view menubar on
gsh -c nao_camera gmenu view menubar on

gsh -c freezer_driver gmenu view menubar on
gsh -c freezer_camera gmenu view menubar on

sleep 5

gsh -c rosbridge roslaunch r3po r3po.launch
sleep 1
gsh -c mjpeg_server rosrun mjpeg_server mjpeg_server
sleep 1
gsh -c turtlesim rosrun turtlesim turtlesim_node
sleep 3
gsh -c turtle_recorder rosrun r3po turtle_recorder.py
sleep 1
gsh -c stage_nodes roslaunch r3po stage_nodes.launch
sleep 1
gsh -c nao_driver roslaunch r3po nao_driver1.launch
# export NAO_IP=10.1.230.102
# export PYTHONPATH=/home/r3po/pynaoqi-python-2.7-naoqi-1.14-linux64/:$PYTHONPATH
sleep 1
gsh -c nao_camera roslaunch r3po nao_camera1.launch
sleep 1
gsh -c freezer_driver roslaunch r3po nao_driver_freezer.launch
sleep 1
gsh -c freezer_camera roslaunch r3po nao_camera_freezer.launch
#sleep 1
#gsh -c turtle_server rosrun r3po turtle_server.py
#sleep 1
#gsh -c stage_server rosrun r3po stage_server.py
#sleep 1
#gsh -c nao_server rosrun r3po nao_server.py
sleep 1
gsh -c turtle_server ssh r3po@10.1.230.115
# rosrun r3po turtle_server.py
sleep 1
gsh -c stage_server ssh r3po@10.1.230.115
# rosrun r3po stage_server.py
sleep 1
gsh -c nao_server ssh r3po@10.1.230.115
# rosrun r3po nao_server.py

