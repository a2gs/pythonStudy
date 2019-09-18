#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class myBaseException(Exception):
	def __init__(self, errNum, errMsg):
		self.err = errNum
		self.msg = errMsg
		
class myExcept_1(myBaseException):
	def __init__(self):
		super().__init__(13, "except 1")

class myExcept_2(myBaseException):
	def __init__(self):
		super().__init__(8, "except 2")

def func(b):
	if(b == 1):
		raise myExcept_1
	elif(b == 2):
		raise myExcept_2
	elif(b == 3):
		return

try:
	func(1)
except myExcept_1 as e:
	print(f'Erro numeber: {e.err} message: {e.msg}')
except myExcept_2 as e:
	print(f'Erro numeber: {e.err} message: {e.msg}')
else:
	print('No exception')
finally:
	print('Do this')

print('Done1\n--------------------')

try:
	func(2)
except myExcept_1 as e:
	print(f'Erro numeber: {e.err} message: {e.msg}')
except myExcept_2 as e:
	print(f'Erro numeber: {e.err} message: {e.msg}')
else:
	print('No exception')
finally:
	print('Do this')

print('Done2\n--------------------')

try:
	func(3)
except myExcept_1 as e:
	print(f'Erro numeber: {e.err} message: {e.msg}')
except myExcept_2 as e:
	print(f'Erro numeber: {e.err} message: {e.msg}')
else:
	print('No exception')
finally:
	print('Do this')
