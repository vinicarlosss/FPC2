class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.father = None
        self.data = data

class RedBlackTree():
    def __init__(self):
        self.Nil = Node(None)
