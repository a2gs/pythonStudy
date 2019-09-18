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
	if(b == True):
		raise myExcept_1
	else:
		raise myExcept_2

try:
	func(True)
except myExcept_1 as e:
	print(f'Erro numeber: {e.err} message: {e.msg}')
except myExcept_2 as e:
	print(f'Erro numeber: {e.err} message: {e.msg}')

try:
	func(False)
except myExcept_1 as e:
	print(f'Erro numeber: {e.err} message: {e.msg}')
except myExcept_2 as e:
	print(f'Erro numeber: {e.err} message: {e.msg}')
