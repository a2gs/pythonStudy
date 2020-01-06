#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from decorators import timer, debug

class mySampleClass:
	@debug
	def __init__(self, max_num):
		self.max_num = max_num

	@debug
	@timer
	def printIt(self, msg):
		print(msg)
		return 13

	@timer
	def waste_time(self, num_times):
		for _ in range(num_times):
			sum([i**2 for i in range(self.max_num)])

tw = mySampleClass(1000)
print('')
i = tw.printIt("Hi!")
print(i)
print('')
tw.waste_time(999)
