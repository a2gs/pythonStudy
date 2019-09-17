#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import cProfile

print('\n1 - Memory usage -----\n')

print('Generator expressions (better):')
g = (i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0)
print(sys.getsizeof(g))

print('---')

print('List comprehension:')
l = [i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0]
print(sys.getsizeof(l))

print('\n2 - CPU usage --------\n')

print('Generator expressions:')
cProfile.run('sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))')

print('---')

print('List comprehension (better):')
cProfile.run('sum([i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0])')
