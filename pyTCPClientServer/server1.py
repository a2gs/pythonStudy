#!/usr/bin/env python3

# Sockets Tutorial with Python 3 part 1 - sending and receiving data: https://youtu.be/Lbfe3-v7yE0
# https://docs.python.org/3/library/socket.html

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket.gethostname(), 9998)
s.bind((socket.gethostname(), 9998))

s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established!")

	clientsocket.send(bytes("Welcome to the server!", "utf-8"))

	clientsocket.close()
