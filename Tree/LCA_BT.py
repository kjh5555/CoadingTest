"""문제에서 Binary 트리 하나와 해당 트리에 속한 두개의 노드가 주어진다
이때 노드의 공통 조상중 가장 낮은 node LCA를 찾아라

      3                          
    5   1
   6 2 0 8
    7 4
input P =5 q= 1

out = 3

     3                          
    5   1
   6 2 0 8
    7 4
input P =5 q= 4

out = 5

     3                          
    5   1
   6 2 0 8
    7 4
input P =6 q= 4

out = 5
"""

class Node:
    def __init__(self, value=0, left=None, right = None):
        self.value=value
        self.left= left
        self.right = right


def LCA(root, p, q):
    if root == None:
        return None
    
    left = LCA(root.left,p,q)
    right = LCA(root.right,p,q)

    if root == p or root == q:
        return root
    
    elif left and right:
        return root
    
    return left or right



root=[3,5,1,6,2,0,8,None,None,7,4]
root = Node(value = 3)
root.left = Node(value = 5)
root.right = Node(value = 1)
root.left.left = Node(value = 6)
root.left.right = Node(value = 2)
root.right.left = Node(value = 0)
root.right.right = Node(value = 8)
root.left.right.left = Node(value = 7)
root.left.right.right = Node(value = 4)

LCA(root,5,1)
print(root.value)