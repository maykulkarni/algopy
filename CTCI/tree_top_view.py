from tree import BinaryTree, Node

top_view = dict()

def traverse_tree(node, horizontal_distance, depth_current):
    if node:
        if horizontal_distance in top_view:
            node_value, depth_old = top_view[horizontal_distance]
            if depth_old > depth_current:
                # this is the higher node
                top_view[horizontal_distance] = (node._data, depth_current)
        else:
            top_view[horizontal_distance] = (node._data, depth_current)
        traverse_tree(node.left, horizontal_distance - 1, depth_current + 1)
        traverse_tree(node.right, horizontal_distance + 1, depth_current + 1)


if __name__ == '__main__':
    tree_one = BinaryTree()
    tree_one._root = Node(1)
    tree_one._root.left = Node(2)
    tree_one._root.right = Node(3)
    tree_one._root.left.right = Node(4)
    tree_one._root.left.right.right = Node(5)
    tree_one._root.left.right.right.right = Node(6)
    traverse_tree(tree_one._root, 0, 1)
    for x in sorted(top_view):
        print(top_view[x][0])
