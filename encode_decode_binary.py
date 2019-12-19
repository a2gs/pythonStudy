#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import sys, os
import struct

print('--- 1 ----------------------------------')

print("ABCD".encode("utf-8"))

print(b"1234".decode("ascii"))

print(b"\x31\x32\x33\x34".decode("ascii"))

print('--- 2 ----------------------------------')
# https://docs.python.org/3/library/struct.html

print(struct.pack("Q", 0x1234))
print(struct.pack(">Q", 0x1234))

print(hex(struct.unpack("Q", b'4\x12\x00\x00\x00\x00\x00\x00')[0]))
print(hex(struct.unpack(">Q", b'\x00\x00\x00\x00\x00\x00\x124')[0]))
