#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from decorators import count_calls_by_function

@count_calls_by_function
def say_whee(msg):
	print(f"Whee {msg}!")

say_whee('aaaaaaaaaaa')
print('')
say_whee('bbbbbbbbbbb')
print('')
say_whee('ccccccccccc')
print('')
