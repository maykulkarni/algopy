class Node:
	_next = None
	_data = None

	def __init__(self, data):
		self._data = data

	def __str__(self):
		return str(self._data)

	def get_next(self):
		return self._next

	def __eq__(self, other):
		return self._data == other._data

	@property
	def next(self):
		return self._next

	@next.setter
	def next(self, new_value):
		self._next = new_value


class LinkedList:
	_head = None
	_tail = None

	def __str__(self):
		temp = self._head
		while temp.get_next() is not None:
			print("{}->".format(temp), end="")
			temp = temp.get_next()
		print(temp)
		return ""

	def add(self, new_data):
		new_node = Node(new_data)
		if self._head is None:
			self._head = new_node
			self._tail = new_node
		else:
			self._tail.set_next(new_node)
			self._tail = self._tail.get_next()

	def remove(self, to_remove):
		temp = self._head
		found = False
		while temp.next is not None:
			if temp.next == to_remove:
				print("Removing: {}".format(temp.next))
		

if __name__ == '__main__':
	a = LinkedList()
	a.add(4)