#!/usr/bin/env python3

# Sockets Tutorial with Python 3 part 2 - buffering and streaming data: https://youtu.be/8A4dqoGL62E
# https://docs.python.org/3/library/socket.html

import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket.gethostname(), 9998)
s.bind((socket.gethostname(), 9998))

s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established!")

	msg = "Welcome to the server!"
	msg = f'{len(msg):<{HEADERSIZE}}' + msg

	clientsocket.send(bytes(msg, "utf-8"))

clientsocket.close()
