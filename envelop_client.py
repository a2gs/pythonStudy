#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import socket
import envelop_sendRecv

con = envelop_sendRecv.connection()

con.connectToServer(socket.gethostname(), 9998, socket.AF_INET, socket.SOCK_STREAM)

msg = 'Ola server!'
con.sendMsg(msg, len(msg))

msgRecv = con.recvMsg()

print(f'Sent: [{msg}] | Received: [{msgRecv}]')

con.endClient()
