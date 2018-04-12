from tree import BinaryTree, Node

top_view = []

def inorder(node):
    if not node.left and not node.right:
        top_view.append(node._data)
    else:
        inorder(node.left)
        inorder(node.right)

if __name__ == '__main__':
    bt = BinaryTree()
    bt._root = Node(20);
    bt._root.left = Node(8);
    bt._root.right = Node(22);
    bt._root.left.left = Node(5);
    bt._root.left.right = Node(3);
    bt._root.right.left = Node(4);
    bt._root.right.right = Node(25);
    bt._root.left.right.left = Node(10);
    bt._root.left.right.right = Node(14);
    inorder(bt._root)
    print(top_view)
