#!/usr/bin/env python3
# -*- coding: utf-8 -*-

md = 5
squaresMod = [(i**2 % md) for i in range(1, 51)]

print(f'From range(1, 51), square mod {md} are:\n{squaresMod}')

print('1 -------------------')

strs1 = ["abc", "bcd", "efg", "hij", "blmn", "opq", "brst", "uvxz"]
bstrs = [strAux2 for strAux2 in strs1 if strAux2.startswith('b')]

print(bstrs)

print('2 -------------------')

s = 5
v = [3, -7, 10]

smul = [s * x for x in v]

print(f'Scalar multiplication: {v} * {s} = {smul}')

print('3 -------------------')

maxS = 5
strs2 = [("abc", 10), ("bcd", 3), ("efg", 5), ("hij", 6), ("lmn", 2), ("opq", 1), ("rst", 4), ("uvxz", 8)]
mstrs = [strAux2 for (strAux2, num2) in strs2 if num2 >= maxS]

print(f'From {strs2}, nodes greater igual {maxS} are: {mstrs}')

print('4 -------------------')

Apoints = [4, 8, 2, 4]
Bpoints = [3, 1, 5, 9]

cartesianProduct = [(a, b) for a in Apoints for b in Bpoints]

print(f'Cartesian product of A points {Apoints} and B {Bpoints}:\n{cartesianProduct}')
