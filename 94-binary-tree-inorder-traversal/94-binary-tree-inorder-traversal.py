# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        Answer = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            Answer.append(root.val)
            dfs(root.right)
            
            return Answer
        return dfs(root)