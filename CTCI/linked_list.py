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
	_length = 0

	def __str__(self):
		if self._length == 0:
			print("List Empty!", end="")
			return ""
		temp = self._head
		while temp.get_next() is not None:
			print("{}->".format(temp), end="")
			temp = temp.get_next()
		print(temp, end="")
		return ""

	def add(self, new_data):
		new_node = Node(new_data)
		if self._head is None:
			self._head = new_node
			self._tail = new_node
		else:
			self._tail.next = new_node
			self._tail = self._tail.next
		self._length += 1

	def remove(self, to_remove):
		if self._length == 0:
			raise ValueError("Empty List")
		elif self._length == 1:
			self._head = None
		elif self._length == 2:
			self._head.next = None
		elif self._head == to_remove:
			self._head = self._head.next
		else:
			temp = self._head
			temp_next = temp.next
			found = False
			while temp_next.next is not None:
				if temp_next == to_remove:
					print("Removing: {}".format(temp.next))
					temp.next = temp_next.next
					temp_next = None
					found = True
					break
				else:
					temp_next = temp_next.next
					temp = temp.next
			if not found:
				if temp_next == to_remove:
					temp.next = None
					found = True
				else:
					print("{} not found in linked list".format(to_remove))
					return
		self._length -= 1

	@property
	def head(self):
		return self._head

	def __len__(self):
		return self._length

	@staticmethod
	def from_array(arr):
		ll = LinkedList()
		for x in arr:
			ll.add(x)
		return ll

	@staticmethod
	def reverse(llist):
		pass


if __name__ == '__main__':
	a = LinkedList.from_array([1, 2, 3])
	a.remove(Node(1))
	print(a)
	a.remove(Node(3))
	print(a)
	a.remove(Node(2))
	print(a)