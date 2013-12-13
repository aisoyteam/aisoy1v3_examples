#!/usr/bin/env python

import roslib;
roslib.load_manifest('aisoy_sdk_tts')
roslib.load_manifest('aisoy_common')

from libaisoy_sdk_tts import *;
from libaisoy_common import *
import rospy

#Init Parameters
tts = Tts(TtsName.Festival)

if __name__ == '__main__':
    rospy.init_node('hello_word')
    tts.setTtsLanguage(Language.English)
    tts.say("Hello Word")
