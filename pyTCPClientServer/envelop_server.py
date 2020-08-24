#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import sys
import socket
import envelop_sendRecv
from signal import signal, SIGILL, SIGTRAP, SIGINT, SIGHUP, SIGTERM, SIGSEGV, SIGUSR1, SIG_IGN, SIGPIPE, SIGIO

def sigHandler(signum, frame):
	if signum == SIGUSR1:
		print('Singal SIGUSR1 received! Normal shutdown returning [0] to shell.\n')
		exit(4)
	else:
		print(f'Singal {signum} received! Return [1] to shell.\n')
		exit(5)

signal(SIGILL , sigHandler)
signal(SIGTRAP, sigHandler)
signal(SIGINT , sigHandler)
signal(SIGHUP , sigHandler)
signal(SIGTERM, sigHandler)
signal(SIGSEGV, sigHandler)
signal(SIGUSR1, sigHandler)
signal(SIGPIPE, sigHandler)
signal(SIGIO, sigHandler)

con = envelop_sendRecv.connection()

ret, retmsg = con.serverLoad(socket.AF_INET, socket.SOCK_STREAM)
if ret == False:
	print(f"Erro: {retmsg}")
	exit(1)

ret, retmsg = con.sockOpts(socket.SO_REUSEADDR)
if ret == False:
	print(f"Erro: {retmsg}")
	exit(1)

ret, retmsg = con.serverBindListen(9998, 5)
if ret == False:
	print(f"Erro: {retmsg}")
	exit(1)

ret, msgret, client = con.serverAccept()
if ret == False:
	print(f"Erro: {retmsg}")
	exit(1)

print(f'Connection from [{client}]')

ret, retmsg, msgRecv = con.recvMsg()
if ret == False:
	print(f"Erro: {retmsg}")
	exit(1)

msg = 'Ola client!'

ret, retmsg = con.sendMsg(msg, len(msg))
if ret == False:
	print(f"Erro: {retmsg}")
	exit(1)

print(f'Received: [{msgRecv}] | Sent: [{msg}]')

con.endClient()
con.endServer()
