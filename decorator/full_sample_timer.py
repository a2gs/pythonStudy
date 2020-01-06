#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from decorators import timer

@timer
def waste_some_time(num_times):
	for _ in range(num_times):
		sum([i**2 for i in range(10000)])


waste_some_time(1)
waste_some_time(999)
