
#깊이 우선 탐색

def dfs(root):
    if root is None:
        return
    
    dfs(root.left)
    dfs(root.right)


