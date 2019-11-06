#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import sys, os

# https://docs.python.org/3/reference/datamodel.html#special-method-names

# All class inherited from 'Object' class

class objTest:
	n = int()
	s = str()

	def __init__(self, nnn, sss):
		self.n = nnn
		self.s = sss

	def __str__(self):
		return(f"My content are: {self.n} and {self.s}")

	def __eq__(self, other):
		print(f'{self.n} == {other.n} and {self.s} == {other.s}')
		return(self.n == other.n and self.s == other.s)

	def __lt__(self, other):
		print(f'{self.n} < {other.n}')
		return(self.n < other.n)

	def __add__(self, other):
		print(f'{self.n} + {other.n}')
		return(self.n + other.n)


sample1 = objTest(10, "abc")
sample2 = objTest(20, "xyz")

print(sample1)
print(sample2)

print("=== 1 ==================================")
print("sample1 + sample2: ")
print(sample1 + sample2)

print("=== 2 ==================================")
print("sample1 == sample2?")
print(sample1 == sample2)

print("=== 3 ==================================")
print("sample1 < sample2?")
print(sample1 < sample2)
