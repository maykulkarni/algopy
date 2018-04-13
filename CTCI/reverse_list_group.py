from linked_list import LinkedList

def print_node(node):
    while(node):
        print(str(node) + "->", end="")
        node = node.next

def reverse(node, k):
    counter = 0
    current = node
    prev = None
    next = None
    while(current is not None and counter < k):
        next = current.next
        current.next = prev
        prev = current
        current = next
        counter += 1

    if next is not None:
        node.next = reverse(next, k)

    return prev


if __name__ == '__main__':
    ll = LinkedList()
    for x in [1, 2, 3, 4, 5, 6, 7, 8]:
        ll.add(x)
    # print_node(ll._head)
    reversed_ll = reverse(ll._head, 3)
    print_node(reversed_ll)
    # print(reversed_ll)
