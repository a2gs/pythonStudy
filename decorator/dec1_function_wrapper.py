#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

def my_decorator(func):
	def wrapper():
		print("Something is happening before the function is called.")
		func()
		print("Something is happening after the function is called.")
	return wrapper

def say_whee():
	print("Whee!")

sc = my_decorator(say_whee)

sc()
