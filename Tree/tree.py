class Node:
    def __init__(self,value=0, left = None, right = None):
        self.value = value;
        self.left = left
        self.right = right

#노드 선언

class BinaryTree:
    def __init__(self):
        self.root= None

bt = BinaryTree()
bt.root = Node(value=1)
bt.root.left = Node(value=2)
bt.root.right = Node(value=3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value=5)
bt.root.right.left = Node(value=6)
bt.root.right.right = Node(value=7)



'''
                   1
                  2 3
                4 5 6 7
                        <도식화>

'''