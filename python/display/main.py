#!/usr/bin/env python

import threading
from gui import Gui
import RPi.GPIO as GPIO
from time import sleep
import socket
from pythonwifi.iwlibs import Wireless
from functions import get_ip
from subprocess import call

#Parameters
SSID='handAssist'
#SSID='Jose Lab'
#pins={1:38,2:40,3:33,4:36,5:37,6:32}  #BOARD numbering
pins={1:20,2:21,3:13,4:16,5:26,6:12}  #BCM numbering
DEBOUNCE_TIME=0.2
TCP_IP = '192.168.1.10'
TCP_PORT = 80
BUFFER_SIZE = 1024

wifi=Wireless('wlan0')

gui=Gui()
gui.start()

while wifi.getEssid()!=SSID:
	pass

while get_ip()=='':
	pass
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
sleep(0.1)
s.send('s')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in pins.values():
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	
def callback1(pin):
	call(['sudo', 'reboot'])
	sleep(DEBOUNCE_TIME)
	
def callback2(pin):
	s.send('f')
	print "hi"
	sleep(DEBOUNCE_TIME)
	
def callback3(pin):
	call(['sudo', 'shutdown','-P','now'])
	sleep(DEBOUNCE_TIME)
	
def callback4(pin):
	s.send('s')
	sleep(DEBOUNCE_TIME)
	
def callback5(pin):
	print pin
	sleep(DEBOUNCE_TIME)
	
def callback6(pin):
	s.send('b')
	sleep(DEBOUNCE_TIME)

sleep(1)	
GPIO.add_event_detect(pins[1], GPIO.BOTH, callback=callback1)
GPIO.add_event_detect(pins[2], GPIO.BOTH, callback=callback2)
GPIO.add_event_detect(pins[3], GPIO.BOTH, callback=callback3)
GPIO.add_event_detect(pins[4], GPIO.BOTH, callback=callback4)
GPIO.add_event_detect(pins[5], GPIO.BOTH, callback=callback5)
GPIO.add_event_detect(pins[6], GPIO.BOTH, callback=callback6)





