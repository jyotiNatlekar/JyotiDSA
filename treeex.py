class Tree:
    def __init__(self,data):
        self.data = data            #instance var(create separate memory for each object)
        self.children = []

    def addChild(self,child):
        self.children.append(child)

    def __str__(self, level=0):
        ret = "   "*level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

#object creation
rootNode = Tree("N1")
n2      = Tree("N2")
n3     = Tree("N3")
n4      = Tree("N4")
n5   = Tree("N5")
n6 = Tree("N6")
n7 = Tree("N7")
n8    = Tree("N8")
n9    = Tree("N9")
n10    = Tree("N10")

rootNode.addChild(n2)
rootNode.addChild(n3)
n2.addChild(n4)
n2.addChild(n5)
n3.addChild(n6)
n3.addChild(n7)
n4.addChild(n9)
n4.addChild(n10)

print(rootNode)