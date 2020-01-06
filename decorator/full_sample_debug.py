#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from decorators import debug

@debug
def make_greeting(name, age=None):
	if age is None:
		return f"Howdy {name}!"
	else:
		return f"Whoa {name}! {age} already, you are growing up!"

print("")
make_greeting("Benjamin")
print("")
make_greeting("Richard", age=112)
print("")
make_greeting(name="Dorrisile", age=116)
print("")
