#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def countdown(num):
	print('Starting')
	while num > 0:
		yield num
		num -= 1

x = 5
val = countdown(x)

for i in range(0, x + 2):
	try:
		print(next(val))
	except StopIteration as e:
		print('End')
