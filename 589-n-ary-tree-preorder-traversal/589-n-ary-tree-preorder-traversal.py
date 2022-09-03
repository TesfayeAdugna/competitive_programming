"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        preorder = []
        def dfs(root):
            if not root.children:
                preorder.append(root.val)
                return preorder
            
            preorder.append(root.val)
            for child in root.children:
                dfs(child)
                
            return preorder
        
        return dfs(root) if root else []