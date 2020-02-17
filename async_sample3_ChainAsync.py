#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://realpython.com/async-io-python/ + myself modifications

import asyncio
import random
import time

async def part1(n: int) -> str:
	i = random.randint(0, 10)
	print(f"{n} part1 sleeping for [{i}] seconds")
	await asyncio.sleep(i)
	result = f"result1"
	print(f"{n} part1 returning [{result}]")
	return result

async def part2(n: int, arg: str) -> str:
	i = random.randint(0, 10)
	print(f"{n} part2 receive [{arg}] and sleeping for [{i}] seconds")
	await asyncio.sleep(i)
	result = f"result2+{arg}"
	print(f"{n} part2 receive [{arg}] returning [{result}]")
	return result

async def chain(n: int) -> None:
	print(f'{n} Starting')
	start = time.perf_counter()
	p1 = await part1(n)
	p2 = await part2(n, p1)
	end = time.perf_counter() - start
	print(f"{n} -->Chained result: [{p2}] (took {end:0.2f} seconds).")

async def main(*args):
	await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
	import sys
	random.seed(444)
	args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
	start = time.perf_counter()
	asyncio.run(main(*args))
	end = time.perf_counter() - start
	print(f"Program finished in {end:0.2f} seconds.")
