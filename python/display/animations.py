from luma.core.virtual import terminal
import time
import sys
import logging
from luma.core import cmdline, error
from pythonwifi.iwlibs import Wireless
from functions import get_ip
import os.path
from PIL import Image

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



class Animator:
	def __init__(self):
		self.device = get_device()
	



	def logoAnimation(self):
		img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'UAEU.png'))
		logo = Image.open(img_path).convert("RGBA")
		fff = Image.new(logo.mode, logo.size, (255,) * 4)

		background = Image.new("RGBA", self.device.size, "white")
		posn = ((self.device.width - logo.width) // 2, 0)
		
		t0=time.time()
		while True:
			for angle in range(0, 360, 2):
				rot = logo.rotate(angle, resample=Image.BILINEAR)
				img = Image.composite(rot, fff, rot)
				background.paste(img, posn)
				self.device.display(background.convert(self.device.mode))
			if (time.time()-t0)>3:
				break

            
            
	
	def welcome_frame(self):
		self.term = terminal(self.device)
		self.term.println("HandAssist V3.1")
		self.term.println("UAEU, IRI Lab")
		time.sleep(2)
		self.term.puts("Connecting ...")



	def waiting_frame(self):
		self.term.puts("|")
		time.sleep(0.5)
		self.term.backspace()
		self.term.puts("/")
		time.sleep(0.5)
		self.term.backspace()
		self.term.puts("-")
		time.sleep(0.5)
		self.term.backspace()
		self.term.puts("\\")
		time.sleep(0.5)
		self.term.backspace()

	def screenUpdateMode(self,mode):
		if mode==0:
			self.term.animate = False
		elif mode==1:
			self.term.animate = True

	def testing(self):
		time.sleep(0.01)
		self.term.clear()
		time.sleep(0.5)
		self.term.println("Connected!")
		self.term.println(get_ip())
		time.sleep(0.5)
