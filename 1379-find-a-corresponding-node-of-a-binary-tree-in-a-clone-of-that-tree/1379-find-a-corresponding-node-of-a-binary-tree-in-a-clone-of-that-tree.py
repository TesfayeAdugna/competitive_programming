# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        
        
        
        
        self.targ = target
        def dfs(cloned):
            if cloned.val == target.val:
                self.targ = cloned
            
            if cloned.left:
                dfs(cloned.left)
            if cloned.right:
                dfs(cloned.right)
                
            return self.targ
        
        return dfs(cloned)
    
    
    
    
    
    
    
    
    