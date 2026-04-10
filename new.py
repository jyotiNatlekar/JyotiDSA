class Node:
    #create node in the tree
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None        #separate memory
    
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self,rootNode,value):
        if value < rootNode.value:
            if rootNode.left is None:
                rootNode.left = Node(value)
            else:
                self.insertNode(rootNode.left, value)
        else:
            if rootNode.right is None:
                rootNode.right = Node(value)
            else:
                self.insertNode(rootNode.right, value)

btobj = BinaryTree()
btobj.insert(50)
btobj.insert(30)
btobj.insert(70)

print(btobj)