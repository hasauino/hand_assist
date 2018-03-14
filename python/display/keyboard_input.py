#!/usr/bin/env python

import socket
from pynput import keyboard




def on_press(key):
	print key

def on_release(key):
	print key



# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
