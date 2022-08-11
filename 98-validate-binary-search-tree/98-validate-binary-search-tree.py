# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def dfs(root, low, high):
            if not root:
                return True
            
            if root.val < high and root.val > low:
                return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
            else:
                return False
            
        return dfs(root, -2147483659, 2147483659)