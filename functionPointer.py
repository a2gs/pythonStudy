#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def myfunc1(a, b):
	return a + b

def myfunc2(a, b, f):
	return(f(a, b))

f = [myfunc1]
print(f[0](2, 2))

print(myfunc2(1, 1, myfunc1))
