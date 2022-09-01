# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root, maxx):
            if not root:
                return
            if root.val >= maxx:
                maxx = root.val
                self.ans += 1
            
            if root.left:
                dfs(root.left, maxx)
            if root.right:
                dfs(root.right, maxx)
                
            return self.ans
        return dfs(root, root.val)