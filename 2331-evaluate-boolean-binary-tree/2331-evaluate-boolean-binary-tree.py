# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root.left:
                return True if root.val == 1 else False
            
            left = dfs(root.left)
            right = dfs(root.right)

            return left and right if root.val == 3 else left or right
            
        return dfs(root)