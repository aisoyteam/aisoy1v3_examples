Introduction
============

In this tutorial it is showed how you can capture an image and save it.

 

The code
========

    !/usr/bin/env python
    
    import roslib; import rospy;
    roslib.load_manifest('aisoy_sdk_camera')
    from libaisoy_sdk_camera import *;
    
    if __name__ == '__main__':
        rospy.init_node('camera_tutorial')
    
        cam = Camera()
        cam.saveFrame("test.jpg")

 

In future updates it will be posted how you can use captures of your camera to make very cool things using OpenCv.