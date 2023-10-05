from binary_tree import Node, BinaryTree

tree = BinaryTree()
tree.setRoot(Node(None, None, None, 20))
tree.getRoot().setLeft(Node(None, Node(None,None,None,25), tree.getRoot(), 15))
pai = tree.getRoot().getLeft()
tree.getRoot().getLeft().getRight().setFather(pai)
print(tree.successor(20).getData())