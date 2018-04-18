import socket
from pynput import keyboard
from time import sleep


TCP_IP = '192.168.1.10'
TCP_PORT = 80
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s.send('s')

def on_press(key):
	
	try:
		if key.char=='u':
			s.send('u')
		elif key.char=='j':
			s.send('j')
		elif key.char=='i':
			s.send('i')
		elif key.char=='k':
			s.send('k')
		elif key.char=='o':
			s.send('o')
		elif key.char=='l':
			s.send('l')

	except AttributeError:
		if key==key.space:
			s.send('s')
		elif key==key.up:
			s.send('f')
		elif key==key.down:
			s.send('b')
		elif key==key.esc:
			s.close()
			return False
    
    
def on_release(key):
	print key


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()

