#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import functools

def do_twice(func):
	def wrapper_do_twice(*args, **kwargs):
		func(*args, **kwargs)
		func(*args, **kwargs)
	return wrapper_do_twice

def do_something_and_return_a_value(func):
	"""
	DECORATOR 4: do_something_and_return_a_value comments
	"""
	def wrapper_do_something_and_return_a_value(*args, **kwargs):
		return func(*args, **kwargs)

	return wrapper_do_something_and_return_a_value

def do_something_functools(func):
	"""
	DECORATOR 5:  do_something_functools comments
	"""
	@functools.wraps(func)
	def wrapper_do_something_functools(*args, **kwargs):
		return func(*args, **kwargs)

	return wrapper_do_something_functools

import time

def timer(func):
	"""Print the runtime of the decorated function"""
	@functools.wraps(func)
	def wrapper_timer(*args, **kwargs):
		start_time = time.perf_counter()    # 1
		value = func(*args, **kwargs)
		end_time = time.perf_counter()      # 2
		run_time = end_time - start_time    # 3
		print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
		return value
	return wrapper_timer

def debug(func):
	"""Print the function signature and return value"""
	@functools.wraps(func)
	def wrapper_debug(*args, **kwargs):
		args_repr = [repr(a) for a in args]                      # 1
		kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
		signature = ", ".join(args_repr + kwargs_repr)           # 3
		print(f"Calling {func.__name__}({signature})")
		value = func(*args, **kwargs)
		print(f"{func.__name__!r} returned {value!r}")           # 4
		return value
	return wrapper_debug


def count_calls_by_function(func):
	@functools.wraps(func)
	def wrapper_count_calls(*args, **kwargs):
		wrapper_count_calls.num_calls += 1
		print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
		return func(*args, **kwargs)
	wrapper_count_calls.num_calls = 0
	return wrapper_count_calls

class count_calls_by_class:
	def __init__(self, func):
		functools.update_wrapper(self, func) # attention here!
		self.func = func
		self.num_calls = 0

	def __call__(self, *args, **kwargs):
		self.num_calls += 1
		print(f"Call {self.num_calls} of {self.func.__name__!r}")
		return self.func(*args, **kwargs)
