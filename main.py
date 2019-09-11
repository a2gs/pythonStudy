#!/usr/bin/env python3

# Mixed code from https://saralgyaan.com/

import main2
import module111
from module222.m222func import m2func
import module222 #just for 'print(module222.__doc__)' line

class sample():
	def __init__(self, _x = 0, _y = ''):
		self.xxx = _x
		self.yyy = _y

	def _get_x(self):
		return self.xxx

	def _get_y(self):
		return self.yyy

	def _set_x(self, _x = 0):
		self.xxx = _x

	def _set_y(self, _y = ''):
		self.yyy = _y

	x = property(_get_x, _set_x)
	y = property(_get_y, _set_y)

def main():

	print('0 ----------------')

	a = sample()
	b = sample()
	c = sample(10, 'abc')

	print('1 ----------------')

	b.x = 13
	b.y = 'xyz'

	print(f'Main function: a = [{a.x}, {a.y!r}] | b = [{b.x}, {b.y!r}] | b = [{c.x}, {c.y!r}]')

	print('2 ----------------')

	m1cinst = module111.m1c()

	print(module111.__doc__)
	print('-')
	print(m1cinst.__doc__)
	print('-')
	print(dir(m1cinst))

	print('3 ----------------')

	print(module222.__doc__) #only possible importing all module ('from module222.m222func import m2func' didn't help): 'import module222'
	print('-')
	print(m2func.__doc__)
	print('-')
	m2func()

if __name__ == "__main__":
	print(f'The name of module two is {__name__}')
	main()
