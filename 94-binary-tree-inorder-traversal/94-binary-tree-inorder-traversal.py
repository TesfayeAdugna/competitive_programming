# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        lst = []
        if not root:
            return lst
        
        def dfs(root):
            if not root.right and not root.left:
                lst.append(root.val)
                return lst
            
            if root.left:
                left = dfs(root.left)
                
            lst.append(root.val)
                
            if root.right:
                right = dfs(root.right)
                
            return lst
        
        return dfs(root)