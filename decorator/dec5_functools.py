#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from decorators import do_something_functools

@do_something_functools
def greet(name):
	"""
	function greet() inside dec5 sample
	"""
	print(f"Hello {name}")
	return 42

str = greet("World")
print(str)

print(f"\n---(functools facility)-------------\nFunc name: {greet.__name__}")
print("help(greet) output: ")
help(greet)
