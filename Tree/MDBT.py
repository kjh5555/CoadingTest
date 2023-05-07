"""문제에서 Binary tree가 주어지는데 해당 tree의 최대깊이를 반환하라"""

from collections import deque


class Node:
    def __init__(self,val = 0,left=None,right=None):
        self.val = val
        self.right =right
        self.left = left


class Binarytree:
    def __init__(self):
        self.root = None
    




def maxDepth(root):
    max_depth = 0
    if root is None:
        return max_depth
    q = deque()
    q.append((root, 1))

    while q:
        cur_node, cur_depth = q.popleft()
       
        max_depth = max(max_depth,cur_depth)
        if cur_node.left:
            q.append((cur_node.left, cur_depth+1))
        elif cur_node.right:
            q.append((cur_node.right, cur_depth+1))


    return max_depth

root = Node(val=3)
root.left=Node(val=9)
root.right=Node(val=20)
root.right.left=Node(val=15)
root.right.right=Node(val=7)
maxDepth(root)
