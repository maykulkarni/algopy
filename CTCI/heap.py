import math

class Heap:
	_arr = [0] * 15
	size = 0

	def __init__(self):
		pass
		# self._arr = [12, 3]
		# self.size = 2

	@staticmethod
	def from_array(arr):
		pass

	def __str__(self):
		return str(self._arr)

	def __len__(self):
		return self.size

	def get_parent_index(self, index):
		return math.ceil(index/2 - 1)

	def get_parent(self, index):
		assert self.has_parent(index)
		return self._arr[self.get_parent_index(index)]

	def left_child_index(self, index):
		return index * 2 + 1

	def right_child_index(self, index):
		return index * 2 + 2

	def left_child(self, index):
		return self._arr[self.left_child_index(index)]

	def right_child(self, index):
		return self._arr[self.right_child_index(index)]

	def add(self, element):
		if self.size == 0:
			self._arr[0] = element
			self.size += 1
		else:
			self._arr[self.size] = element
			self.size += 1
			self.heapify_up()
		print(self._arr)

	def element_at(self, index):
		return self._arr[index]

	def has_parent(self, index):
		return index != 0

	def has_child(self, index):
		pass

	def swap(self, index_one, index_two):
		self._arr[index_one], self._arr[index_two] = \
					self._arr[index_two], self._arr[index_one]

	def heapify_up(self):
		current_index = self.size - 1
		while (self.has_parent(current_index)
				and self.get_parent(current_index) > self.element_at(current_index)):
			self.swap(current_index, self.get_parent_index(current_index))
			current_index = self.get_parent_index(current_index)

	def get_min(self):
		min_element = self._arr[0]
		self.heapify_down()
		return min_element

	def heapify_down(self):
		current_index = 0
		while (self._arr):
			pass

if __name__ == '__main__':
	# heap = Heap()
	# for i in reversed(range(5, 10)):
	# 	heap.add(i)
	# print(heap)
	# print(len(heap))
