#!/usr/bin/env python3

# Sockets Tutorial with Python 3 part 1 - sending and receiving data: https://youtu.be/Lbfe3-v7yE0
# https://docs.python.org/3/library/socket.html

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 9998))

full_msg = ''

while True:
	msg = s.recv(5)
	if len(msg) <= 0:
		break

	full_msg += msg.decode("utf-8")


print(full_msg)
