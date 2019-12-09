#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('1 -------------------')

def myfunc1(a, b):
	return a + b

def myfunc2(a, b, f):
	return(f(a, b))

f = [myfunc1]
print(f[0](2, 2))

print(myfunc2(1, 1, myfunc1))

print('2 -------------------')

def thirdF():
	return "ccc"

def parent(num):
	def first_child(): #inner parent function
		return "aaa"

	def second_child():
		return "bbb"

	if num == 1: #inner parent function
		return first_child
	else:
		return second_child

first = parent(1)
second = parent(2)
third = thirdF

print(first())
print(second())
print(third())
