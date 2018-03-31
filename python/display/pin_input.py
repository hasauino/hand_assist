import RPi.GPIO as GPIO
from time import sleep
import socket

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


pins={1:38,2:40,3:33,4:36,5:37,6:32}
DEBOUNCE_TIME=0.2

for pin in pins.values():
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	
def callback1(pin):
	print pin
	sleep(DEBOUNCE_TIME)
	
def callback2(pin):
	print pin
	sleep(DEBOUNCE_TIME)
	
def callback3(pin):
	print pin
	sleep(DEBOUNCE_TIME)
	
def callback4(pin):
	print pin
	sleep(DEBOUNCE_TIME)
	
def callback5(pin):
	print pin
	sleep(DEBOUNCE_TIME)
	
def callback6(pin):
	print pin
	sleep(DEBOUNCE_TIME)
	
GPIO.add_event_detect(pins[1], GPIO.BOTH, callback=callback1)
GPIO.add_event_detect(pins[2], GPIO.BOTH, callback=callback2)
GPIO.add_event_detect(pins[3], GPIO.BOTH, callback=callback3)
GPIO.add_event_detect(pins[4], GPIO.BOTH, callback=callback4)
GPIO.add_event_detect(pins[5], GPIO.BOTH, callback=callback5)
GPIO.add_event_detect(pins[6], GPIO.BOTH, callback=callback6)


sleep(100)
