#!/usr/bin/env python
import roslib; roslib.load_manifest('aisoy_sdk_asr')
import roslib; roslib.load_manifest('aisoy_sdk_tts')
roslib.load_manifest('aisoy_common')
from libaisoy_sdk_asr import *;
from libaisoy_sdk_tts import *;
from libaisoy_common import *
import rospy


    #Init Parameters

asr = Asr()
tts = Tts()


if __name__ == '__main__':
	rospy.init_node('parrot')
	tts.setTtsLanguage(Language.English)
	asr.setAsrLanguage(Language.English)
	print "...Listening..."
	asr.startListening()
	tts.say("Tell me something and I will repeat it")
	while not rospy.is_shutdown():
		print "Say something..."
		listened = asr.listen()
		if listened:
			print "- Listened: " + str(listened)
			tts.say(str(listened))
			if (str(listened) == "stop"):
	                        break
	tts.say("Goodbye")
	asr.stopListening()

