#!/usr/bin/env python

import os
import time
import threading
from pythonwifi.iwlibs import Wireless
from subprocess import call
from animations import Animator
SSID='handAssist'
#SSID='Jose Lab'






class Gui (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.animator=Animator()
	
    def run(self):
        self.animator.logoAnimation()
        self.animator.welcome_frame()
        wifi=Wireless('wlan0')
        while wifi.getEssid()=="":
            waiting_frame()

        self.animator.screenUpdateMode(1)
        while True:
            self.animator.testing()
            time.sleep(5)


						
