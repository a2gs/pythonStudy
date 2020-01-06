#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from decorators import do_twice, do_something_and_return_a_value

@do_something_and_return_a_value
def greet(name):
	"""
	function greet() inside dec4 sample
	"""
	print(f"Hello {name}")
	return 42

str = greet("World")
print(str)

print(f"\n---(continues to dec5)-------------\nFunc name: {greet.__name__}")
print("help(greep) output (is not, help() output from decorator): ")
help(greet)
