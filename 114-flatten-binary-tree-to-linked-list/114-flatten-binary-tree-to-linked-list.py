# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        head = root
        
        
        head
        
        """
        self.temp = None
        def dfs(root):
            if not root:
                return
            
            dfs(root.right)
            dfs(root.left)
            
            root.right = self.temp
            root.left = None
            self.temp = root

        dfs(root)
        
        
        
        