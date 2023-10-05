class Node:

    def __init__(self):
        self.left = None
        self.right = None
        self.father = None
        self.data = None

    def getData(self):
        return self.data
    
    def setData(self):
        return self.data
    
    def getLeft(self):
        return self.left
    
    def setLeft(self, n):
        self.left = n
    
    def getRight(self):
        return self.right

    def setRight(self, n):
        self.right = n

    def getFather(self):
        return self.father
    
    def setFather(self, n):
        self.father = n
    
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