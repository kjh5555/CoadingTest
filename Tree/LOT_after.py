class Node:
    def __init__(self,val = 0,left=None,right=None):
        self.val = val
        self.right =right
        self.left = left


def maxDepth(root):
    max_depth = 0

    if root is None:
        return max_depth
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    max_depth = max(left_depth,right_depth) + 1
    return max_depth




root = Node(val=3)
root.left=Node(val=1)
root.right=Node(val=2)
root.right.left=Node(val=1)
root.right.right=Node(val=1)

print(maxDepth(root))