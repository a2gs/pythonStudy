#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

def addn(n):
	return n + n

def addnm(n, m):
	return n + m

def even(n) -> bool:
	if n % 2 == 0:
		return True

	return False


m1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
m3 = [1.1, 2.2, 3.3, 4.4, 5.5]

print('---------------------\nZIP')
[print(i) for i in zip(m1, m2)]
[print(i) for i in zip(m1, m2, m3)]

print('---------------------\nMAP')
ret1 = map(addn, m1)
print(list(ret1))

ret2 = map(lambda x, y: x + y, m1, m3)
print(list(ret2))

print('---------------------\nREDUCE')
from functools import reduce
print(reduce(addnm, m1, 20))
print(reduce(addnm, m2, 'Init: '))

print('---------------------\nFILTER')
evenm = filter(even, m1)
print(list(evenm))
