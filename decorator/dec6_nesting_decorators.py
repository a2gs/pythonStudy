#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from decorators import debug, do_twice, timer

print('---1-----------------------')

# As: debug(do_twice(greet()))

@debug
@do_twice
def greet1(name):
	print(f"Hello {name}")

greet1('Andre 1')

print('---2-----------------------')

# Here, do_twice() calls 2x debug(greet2())

@do_twice
@debug
def greet2(name):
    print(f"Hello {name}")

greet2('Andre 2')
