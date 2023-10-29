from binary_tree import Node, BinaryTree

class Node(Node):
    def __init__(self, left, right, father, data):
        super().__init__(left, right, father, data)
        self.height = 1


class AvlTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def getHeight(self, node):
        if not node:
            return 0
        return node.height
    
    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.getLeft()) - self.getHeight(node.getRight())

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
        
        node.height = 1 + max(self.getHeight(node.getLeft()), self.getHeight(node.getRight()))
        y.height = 1 + max(self.getHeight(y.getLeft()), self.getHeight(y.getRight()))

    def rightRotate(self, node):
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
        node.height = 1 + max(self.getHeight(node.getLeft()), self.getHeight(node.getRight()))
        y.height = 1 + max(self.getHeight(y.getLeft()), self.getHeight(y.getRight()))
    
    def insert(self, root, key):
        if not root:
            self.setRoot(Node(None,None,None, key))
            return
        if key < root.getData():
            root.setLeft(self.insert(root.getLeft(), key))
        else:
            root.setRight(self.insert(root.getRight(), key))
        
        root.height = 1 + max(self.getHeight(root.getLeft()), self.getHeight(root.getRight()))

        balance = self.getBalance(root)

        if balance > 1:
            if key < root.left.getData():
                return self.rightRotate(root)
            else:
                root.setLeft(self.leftRotate(root.getLeft()))
                return self.rightRotate(root)
        
        if balance < -1:
            if key > root.right.getData():
                return self.leftRotate(root)
            else:
                root.setRight(self.rightRotate(root.getRight()))
                return self.leftRotate(root)