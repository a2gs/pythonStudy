#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://realpython.com/async-io-python/ + myself modifications

import asyncio
import time

def aaa():
	print('1')

def bbb():
	print('2')

async def ccc():
	print('3')

async def count():
	print("One")
	aaa()

	await asyncio.sleep(1)

	print("Two")
	bbb()

async def main():
	await asyncio.gather(count(), count(), ccc(), count(), count())

if __name__ == "__main__":
	s = time.perf_counter()
	asyncio.run(main())
	elapsed = time.perf_counter() - s
	print(f"{__file__} executed in {elapsed:0.2f} seconds.")
