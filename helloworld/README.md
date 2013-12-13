Introduction
============

The simplest tutorial in python consists of Aisoy say Hello Word using tts (Text To Speech) module.


HelloWord.py
============

First of all, it imports libraries and initializes modules that we use. In this case, it uses tts to say "Hello Word". Then, it creates the main class with the following steps: initialize a node ros, set tts language and run it.

Here it is shown the code. 

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

 

Instructions for running a simple application
=============================================

1. Create a Python file .py with the code. For example : HelloWord.py
2. Execute: python HelloWord.py