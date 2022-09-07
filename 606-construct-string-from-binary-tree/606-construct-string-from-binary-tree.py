# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            Answer = ""
            if not root: return Answer
            
            Answer += str(root.val)
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left or right:
                Answer += "(" + left + ")"
                if right:
                    Answer += "(" + right + ")"
            return Answer
        
        return dfs(root)