#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import socket
import envelop_sendRecv

con = envelop_sendRecv.connection()

con.serverLoad(socket.AF_INET, socket.SOCK_STREAM)

con.sockOpts(socket.SO_REUSEADDR)

con.serverBindListen(9998, 5)

client = con.serverAccept()

print(f'Connection from [{client}]')

msgRecv = con.recvMsg()

msg = 'Ola client!'

con.sendMsg(msg, len(msg))

print(f'Received: [{msgRecv}] | Sent: [{msg}]')

con.endClient()
con.endServer()
