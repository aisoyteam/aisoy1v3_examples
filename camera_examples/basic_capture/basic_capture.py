!/usr/bin/env python

import roslib; import rospy;
roslib.load_manifest('aisoy_sdk_camera')
from libaisoy_sdk_camera import *;
    
if __name__ == '__main__':
    rospy.init_node('camera_tutorial')
    cam = Camera()
    cam.saveFrame("test.jpg")