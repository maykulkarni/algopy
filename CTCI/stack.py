import random


class Stack:
	_arr = []
	_pointer = -1
	_size = 0
	_load = 0.8
	_capacity = 10

	def __init__(self):
		self._arr = [0] * self._capacity

	def _ensure_capacity(self):
		if self._size > self._load * self._capacity:
			new_capacity = 2 * self._capacity
			_new_arr = [0] * new_capacity
			for i, x in enumerate(self._arr):
				_new_arr[i] = self._arr[i]
			self._arr = _new_arr
			print("Resized Stack from {} to {}".format(self._capacity,
													   new_capacity))
			self._capacity = new_capacity
		elif self._size < (0.2 * self._capacity) and self._size > 20:
			new_capacity = self._capacity // 2
			_new_arr = [0] * new_capacity
			for i in range(self._size):
				_new_arr[i] = self._arr[i]
			self._arr = _new_arr
			print("Resized Stack from {} to {}".format(self._capacity,
													   new_capacity))
			self._capacity = new_capacity

	def add(self, item):
		self._ensure_capacity()
		self._pointer += 1
		self._size += 1
		self._arr[self._pointer] = item

	def pop(self):
		self._ensure_capacity()
		if self._size == 0:
			return ValueError("Size is 0")
		to_return = self._arr[self._pointer]
		self._pointer -= 1
		self._size -= 1
		return to_return

	def __str__(self):
		return self._arr.__str__()

if __name__ == '__main__':
	stack = Stack()
	for _ in range(1000):
		stack.add(100)
	for _ in range(1000):
		stack.pop()
	print(stack)
