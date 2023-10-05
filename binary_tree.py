class Node:

    def __init__(self,left, right, father, data):
        self.left = left
        self.right = right
        self.father = father
        self.data = data

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getLeft(self):
        return self.left
    
    def setLeft(self, node):
        self.left = node
    
    def getRight(self):
        return self.right

    def setRight(self, node):
        self.right = node

    def getFather(self):
        return self.father
    
    def setFather(self, node):
        self.father = node
    
    def isLeft(self):
        father = self.getFather()
        if father == None:
            return False
        if father.getLeft() == self:
            return True
        return False 
    
    def isRight(self):
        father = self.getFather()
        if father == None:
            return False
        if father.getRight() == self:
            return True
        return False
    
    def isBrother(self):
        father = self.getFather()
        if father == None:
            return False
        if self.isLeft():
            return father.getRight()
        return father.getLeft()


class BinaryTree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root
    
    def setRoot(self, node):
        self.root = node

    def search(self, node, element):
        if node == None or element == node.data:
            return node
        if element < node.data:
            return self.search(node.getLeft(), element)
        return self.search(node.getRight(), element)
    
    def minimum(self):
        node = self.getRoot()
        while node.getLeft() is not None:
            node = node.getLeft()
        return node
    
    def maximum(self):
        node = self.getRoot()
        while node.getRight() is not None:
            node = node.getRight()
        return node