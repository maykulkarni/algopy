class Node:
    left = None
    right = None
    _data = None

    def __init__(self, data):
        self._data = data

    def __str__(self):
        return str(self._data)

class BinaryTree:
    _root = None

    def __init__(self):
        self.maximum_path_sum_val = float("-inf")

    def __str__(self):
        self._inorder(self._root)
        return ""

    def inorder(self):
        self._inorder(self._root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node)
            self._inorder(node.right)

    def preorder(self):
        self._preorder(self._root)

    def _preorder(self, node):
        if node:
            print(node)
            self._preorder(node.left)
            self._preorder(node.right)

    def traverse_tree(self, node):
        if not node:
            return 0
        # traverse left tree
        left_depth = self.traverse_tree(node.left) + 1
        # traverse right tree
        right_depth = self.traverse_tree(node.right) + 1
        # select the maximum
        max_depth = max(left_depth, right_depth)
        return max_depth

    def max_depth(self):
        if not self._root:
            print("Tree is empty")
            return
        return self.traverse_tree(self._root)

    def _maximum_path_sum(self, node):
        if not node:
            return 0

        left_max = self._maximum_path_sum(node.left)
        right_max = self._maximum_path_sum(node.right)

        best_single_path = max(left_max, right_max)

        best_single_path_including_root = max(node._data,
                                              node._data + best_single_path)

        best_path_including_all_nodes = max(best_single_path_including_root,
                                            left_max + right_max + node._data)

        if self.maximum_path_sum_val < best_path_including_all_nodes:
            self.maximum_path_sum_val = best_path_including_all_nodes

        return best_single_path_including_root

    def maximum_path_sum(self):
        self._maximum_path_sum(self._root)
        return self.maximum_path_sum_val


class BinarySearchTree(BinaryTree):
    def __init__(self):
        pass

    def add(self, element):
        if self._root is None:
            self._root = element
        else:
            correct_position_found = False
            correct_position = ""
            pointer = self._root
            while not correct_position_found:
                if element._data >= pointer._data:
                    if pointer.right is not None:
                        pointer = pointer.right
                    else:
                        correct_position_found = True
                        correct_position = "right"
                else:
                    if pointer.left is not None:
                        pointer = pointer.left
                    else:
                        correct_position_found = True
                        correct_position = "left"

            assert correct_position is not ""
            if correct_position == "left":

                pointer.left = element
            else:
                pointer.right = element


if __name__ == "__main__":
    bt = BinaryTree()
    bt._root = Node(10)
    bt._root.left = Node(2)
    bt._root.right   = Node(10);
    bt._root.left.left  = Node(20);
    bt._root.left.right = Node(1);
    bt._root.right.right = Node(-25);
    bt._root.right.right.left   = Node(3);
    bt._root.right.right.right  = Node(4);
    bt.preorder()
