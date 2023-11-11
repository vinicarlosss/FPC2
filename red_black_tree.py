class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.father = None
        self.data = data
        self.color = None

class RedBlackTree():

    def __init__(self):
        self.Nil = Node(None)
        self.root = None
    

    def leftRotate(self, node):
        y = node.right
        node.right = y.left
        if y.left is not None:
            y.left.father = node
        y.father = node.father
        if node.father == self.Nil:
            self.root = y
        elif node == node.father.left:
            node.father.left = y
        else:
            node.father.right = y
            y.left = node
            node.father = y
    

    def rightRotate(self, node):
        y = node.left
        node.left = y.right
        if y.right is not None:
            y.right.father = node
        y.father = node.father
        if node.father == self.Nil:
            self.root = y
        elif node == node.father.right:
            node.father.right = y
        else:
            node.father.left = y
            y.right = node
            node.father = y


    def insertFixup(self, node):
        while node.father.color == "RED":
            if node.father == node.father.father.left:
                y = node.father.father.right
                if y.color == "RED":
                    node.father.color = "BLACK"
                    y.color = "BLACK"
                    node.father.father.color = "RED"
                    node = node.father.father
                elif node == node.father.right:
                    node = node.father
                    self.leftRotate(node)
                    node.father.color = "BLACK"
                    node.father.father.color = "RED"
                    self.rightRotate(node.father.father)
            else:
                y = node.father.father.left
                if y.color == "RED":
                    node.father.color = "BLACK"
                    y.color = "BLACK"
                    node.father.father.color = "RED"
                    node = node.father.father
                elif node == node.father.right:
                    node = node.father
                    self.leftRotate(node)
                    node.father.color = "BLACK"
                    node.father.father.color = "RED"
                    self.rightRotate(node.father.father)
        self.root.color = "BLACK"
                    

    def insert(self, node):
        y = self.Nil
        x = self.root
        while x is not self.Nil:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        node.father = y
        if y == self.Nil:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
            node.left = self.Nil
            node.right = self.Nil
            node.color = "RED"
            self.insertFixup(self, node)