#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from decorators import do_twice

@do_twice
def say_whee():
	print("Whee!")

@do_twice
def greet(name):
	print(f"Hello {name}")

say_whee()
greet("World")
