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
    
    def minimum(self, node):
        while node.getLeft() is not None:
            node = node.getLeft()
        return node
    
    def maximum(self, node):
        while node.getRight() is not None:
            node = node.getRight()
        return node
    
    def successor(self, element):
        node = self.search(self.getRoot(), element)
        if node == None:
            return node
        if node.getRight() is not None:
            return self.minimum(node.getRight())
        y = node.getFather()
        while y is not None and node == y.getRight():
            node = y
            y = y.getFather()
        return y
    

    def InOrderTreeWalk(self,x):
        if x is not None:
            self.InOrderTreeWalk(x.getLeft())
            print(x.getData())
            self.InOrderTreeWalk(x.getRight())

    
    def insert(self, node):
        y = None
        x = self.getRoot()
        while x is not None:
            y = x
            if node.getData() < x.getData():
                x = x.getLeft()
            else:
                x = x.getRight()
        node.setFather(y)
        if y == None:
            self.setRoot(node)
        elif node.getData() < y.getData():
            y.setLeft(node)
        else:
            y.setRight(node)


    def Transplant(self, u, v):
        if u.getFather() is None:
            self.setRoot(v)
        elif u == u.getFather().getLeft():
            u.getFather().setLeft(v)
        else:
            u.getFather().setRight(v)
        if v is not None:
            v.setFather(u.getFather())
    

    def TreeDelete(self, z):
        if z.getLeft() is None:
            self.Transplant(z, z.getRight())
        elif z.getRight() is None:
            self.Transplant(z,z.getLeft())
        else:
            y = self.minimum(z.getRight())
            if y.getFather() != z:
                self.Transplant(y,y.getRight())
                y.setRight(z.getRight())
                y.getRight().setFather(y)
            self.Transplant(z,y)
            y.setLeft(z.getLeft())
            y.getLeft().setFather(y)