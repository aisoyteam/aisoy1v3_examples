Tutorial: AISoy repeats anything you say (in Python)
====================================================

Release date: 9 Oct 2013
Author: Eva Garcia, egarcia@aisoy.com

Introduction
------------

The main objective of this tutorial is to implement simple application in which AISoy listen to what you say and repeats them. Main modules used are asr (Automatic Speech Recognition) to listen and tts(Text to Speach) to speak.

In main method,  the most important thing is to establish the language of  modules, that Aisoy start listening, heard something and answer. 

Additionally, if AIsoy recognizes "stop", say goodbye, stops listening and terminates.

Code
----


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