#!/usr/bin/env python3

import cProfile

def func(x):
	print(f"Hello {x:d}")

	numbers = []
	start = 0

	for i in range(x):
		print(i)
		numbers.append(i)

cProfile.run('func(100000)')
