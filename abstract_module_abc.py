#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Automobile(ABC):
	"""Formal interface: Abstract automobile class."""

	@abstractmethod
	def start(self):
		pass

	@abstractmethod
	def accelerate(self):
		pass

	@abstractmethod
	def stop(self):
		pass

class Car(Automobile):
	"""Concrete Class: Car"""

	def start(self):
		return "The car is starting"

	def accelerate(self):
		return "The car is accelerating"

	def stop(self):
		return "The car is stopping"


class Truck(Automobile):
	"""Concrete Class: Truck"""

	def start(self):
		return "The truck is starting"

	def accelerate(self):
		return "The truck is accelerating"

	def stop(self):
		return "The truck is stopping"


class Bus(Automobile):
	"""Concrete Class: Bus"""

	def start(self):
		return "The bus is starting"

	def accelerate(self):
		return "The bus is accelerating"

	def stop(self):
		return "The bus is stopping"

class classDummy():
	def __init__(self):
		if self.__class__ == classDummy:
			raise NotImplementedError("Interfaces can't be instantiated")
	def func(self):
		pass

class classDummyDeriv(classDummy):
	def __init__(self):
		print("Dummy class _init__ ok")
	def func(self):
		print("Dummy class func ok")


car = Car()
truck = Truck()
bus = Bus()

print(car.start())
print(car.accelerate())
print(car.stop())
print(truck.start())
print(truck.accelerate())
print(truck.stop())
print(bus.start())
print(bus.accelerate())
print(bus.stop())

c1 = classDummy() # ERROR
c2 = classDummyDeriv()
