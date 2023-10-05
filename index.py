from binary_tree import Node, BinaryTree

tree = BinaryTree()
tree.setRoot(Node(None, None, None, 20))
tree.getRoot().setRight(Node(None, None, None, 30))
print(tree.minimum().getData())