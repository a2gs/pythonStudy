#!/usr/bin/env python3

# Sockets Tutorial with Python 3 part 2 - buffering and streaming data - https://youtu.be/8A4dqoGL62E
# https://docs.python.org/3/library/socket.html

import socket
import struct

HEADERSIZE = 4

def readOneMsg(sckt, recvBuf):
	msgSz = 0
	nBytesReaded = b''
	recvBuf = b''
	chunk = b''

	while len(nBytesReaded) < HEADERSIZE:

		chunk = sckt.recv(HEADERSIZE - len(nBytesReaded))

		if chunk == b'':
			raise RuntimeError("socket connection broken")

		nBytesReaded = nBytesReaded + chunk

	#msgSz = int(socket.ntohl(nBytesReaded))
	msgSz = struct.unpack('!4I', nBytesReaded)
	print(f'Msg size: {msgSz}')

	while len(recvBuf) < msgSz:

		chunk = sckt.recv(msgSz - len(recvBuf))

		if chunk == b'':
			raise RuntimeError("socket connection broken")

		recvBuf = recvBuf + chunk

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((socket.gethostname(), 9998))

	while True:

		msg = ''

		while True:
			readOneMsg(s, msg)

			print(f'Message: {msg.decode("utf-8")}')

if __name__ == "__main__":
	main()
