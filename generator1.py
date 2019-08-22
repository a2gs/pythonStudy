#!/usr/bin/env python3

'''
From Pythonest YT channel
'''

def myGen():
	n = 1
	print("First")
	yield n

	n += 1
	print("Second")
	yield n

	n += 1
	print("Last")
	yield n

for i in myGen():
	print(i)
