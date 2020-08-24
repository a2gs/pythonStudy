#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import socket
import envelop_sendRecv

con = envelop_sendRecv.connection()

ret, retmsg = con.connectToServer(socket.gethostname(), 9998, socket.AF_INET, socket.SOCK_STREAM)
if ret == False:
	print(f"Erro: {retmsg}")
	exit(1)


msg = 'Ola server!'
ret, retmsg = con.sendMsg(msg, len(msg))
if ret == False:
	print(f"Erro: {retmsg}")
	exit(1)


ret, retmsg, msgRecv = con.recvMsg()
if ret == False:
	print(f"Erro: {retmsg}")
	exit(1)


print(f'Sent: [{msg}] | Received: [{msgRecv}]')

con.endClient()
