#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from decorators import count_calls_by_class

@count_calls_by_class
def say_whee():
	print("Whee!")

say_whee()
print('')
say_whee()
print('')
say_whee()
print('')
