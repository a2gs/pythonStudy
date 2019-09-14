#!/usr/bin/env python3

import cProfile
import timeit

def func(x):
	print(f"Hello {x:d}")

	numbers = []
	start = 0

	for i in range(x):
		print(i)
		numbers.append(i)

cProfile.run('func(100000)')

#Or: print(timeit.timeit('func(100000)', globals=globals(), number=1))
print(timeit.timeit('func(100000)', setup="from __main__ import func", number=1))
