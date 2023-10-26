from binary_tree import Node, BinaryTree

class Node(Node):
    def __init__(self, left, right, father, data):
        super().__init__(left, right, father, data)
        self.balancingFactor = 0


class AvlTree(BinaryTree):
    def __init__(self):
        super().__init__()
    

    def leftRotate(self, node):
        y = node.getRight()#20
        node.setRight(y.getLeft())#none
        if y.getLeft() != None:
            y.getLeft().setFather(node)#10
        y.setFather(node.getFather())#none
        if node.getFather() == None:
            self.setRoot(y)#20
        elif node == node.getFather().getLeft():
            node.getFather().setLeft(y)
        else: 
            node.getFather().setRight(y)
            y.setLeft(node)
            node.setFather(y)
    

    def leftRight(self, node):
        y = node.getLeft()
        node.setLeft(y.getRight())
        if y.getRight() != None:
            y.getRight().setFather(node)
        y.setFather(node.getFather())
        if node.getFather() == None:
            self.setRoot(y)
        elif node == node.getFather().getRight():
            node.getFather().setRight(y)
        elif node.getFather().getLeft() == y:
            y.setRight(node)
            node.setFather(y)