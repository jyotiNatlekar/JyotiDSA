''' tree - nonlinear DS
binary tree -- has upto 2 child
1.full binary tree -- each node has either 0 or 2 child , no node has single child
2.complete binary tree -- all levels except possibly the last are completely filled , 
                          nodes in last level are filled from left to right 
3.perfect binary tree -- all internal nodes have exactly two nodes , 
                         all leaf nodes are at same level
'''
# --- tree using list --- 
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
rootNode = Tree("Drinks")
hot      = Tree("Hot")
cold     = Tree("Cold")
tea      = Tree("Tea")
coffee   = Tree("Coffee")
nonAlcoholic = Tree("NonAlcoholic")
alcoholic    = Tree("Alcoholic")

rootNode.addChild(hot)
rootNode.addChild(cold)
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(alcoholic)
cold.addChild(nonAlcoholic)

print(rootNode)