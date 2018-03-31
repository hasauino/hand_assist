#!/usr/bin/env python

import os
import time
import threading
from luma.core.virtual import terminal
import sys
import logging
from luma.core import cmdline, error
from pythonwifi.iwlibs import Wireless
from subprocess import call
from functions import get_ip
SSID='handAssist'
#SSID='Jose Lab'


def get_device(actual_args=None):
    """
    Create device from command-line arguments and return it.
    """

    actual_args = ['--interface', 'spi', '--d', 'ssd1306']
    parser = cmdline.create_parser(description='luma.examples arguments')
    args = parser.parse_args(actual_args)
    if args.config:
        # load config from file
        config = cmdline.load_config(args.config)
        args = parser.parse_args(config + actual_args)

    # create device
    try:
        device = cmdline.create_device(args)
    except error.Error as e:
        parser.error(e)

    return device






class Gui (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.device = get_device()
	def run(self):
		while True:
				term = terminal(self.device)
				term.println("HandAssist V3.1")
				term.println("UAEU, IRI Lab")
				time.sleep(2)
				wifi=Wireless('wlan0')
				term.puts("Connecting ...")
				while wifi.getEssid()!=SSID:
					term.puts("|")
					time.sleep(0.5)
					term.backspace()
					term.puts("/")
					time.sleep(0.5)
					term.backspace()
					term.puts("-")
					time.sleep(0.5)
					term.backspace()
					term.puts("\\")
					time.sleep(0.5)
					term.backspace()
				term.clear()
				time.sleep(0.5)
				term.println("Connected!")
				term.println(get_ip())
				time.sleep(0.5)
				while True:
					pass
						
