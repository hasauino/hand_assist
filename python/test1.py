#!/usr/bin/env python

import socket


TCP_IP = '192.168.1.10'



TCP_PORT = 80
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s.send('s')

s.close()
