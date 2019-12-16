#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 'args' at sumIntNumbers() is just a name (a tuple! Immutable), it can be anything else (ex: def sumIntNumbers(*numbers))
def sumIntNumbers(*args):
	ret = 0

	#Erro
	#args[2] = 10

	for i in args:
		ret += i

	return ret

# 'kwargs' at concatenate() is just a name (a dict mutable!), it can be anything else (ex: def concatenate(**stringsToConcatenate))
def concatenate(**kwargs):
	ret = "Name: "
	ret += kwargs["name"]

	birth = kwargs["birth"]
	bbirth = birth[0]
	mbirth = birth[1]
	ybirth = birth[2]
	ret += f", Birth: {bbirth}/{mbirth}/{ybirth}, "

	kwargs["luckyNumber"] = 8
	ret += "Lucky number: " + str(kwargs["luckyNumber"])

	return ret

# Error defining 'kwargs' before 'args'
def func(a, b, c, *args, **kwargs):
	print(f'Function with \'args\' and \'kwargs\' together: a = {a} | b = {b} | c = {c} | args = {args} | kwargs = {kwargs}')


print('1 ---------------')

x = sumIntNumbers(1, 2, 3, 4, 5)
print(f'sumIntNumbers = {x}')

# Error (list to int at ret += i into sumIntNumbers()):
#x = sumIntNumbers([1, 2, 3, 4, 5])
#print(f'sumIntNumbers = {x}')

print('2 ---------------')

y = concatenate(name = 'Andre', birth = [13, 8, 1981], luckyNumber = 13)
print(f'concatenate = {y}')

print('3 ---------------')

func(1, 'asd', 13.8, 'qwe', 'zxc', p = 10, q = 100)

print('4 ---------------')
print('Unpacking \'*\' and \'**\':')
l1 = ['asd', 'qwe', 'zxc', 'wer']
l2 = [*"Andre Augusto Giannotti Scota"]
d1 = {'a' : 10, 'b' : 100, 'c' : 1000, 'd' : 10000}
d2 = {'x' : -1, 'y' : -10}
d = {**d1, **d2}

print(*l1)
print(*d1)
print(*d2)
print(*d)
print(l2)
