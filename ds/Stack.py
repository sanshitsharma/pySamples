#!/usr/bin/python

class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.isEmpty():
			return self.items.pop()		
		return None

	def peek(self):
		if not self.isEmpty():
			return self.items[len(self.items)-1]
		return None

	def size(self):
		return len(self.items)

        @property
	def isEmpty(self):
		return self.items == []

