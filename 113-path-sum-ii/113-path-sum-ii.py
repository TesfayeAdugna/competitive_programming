# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.answer = []
        def dfs(root, path, pathSum):
            if not root:
                return
            if not root.left and not root.right:
                if pathSum + root.val == targetSum:
                    path.append(root.val)
                    self.answer.append(path)
                return self.answer
            
            path.append(root.val)
            if root.left:
                dfs(root.left, list(path), pathSum + root.val)
            if root.right:
                dfs(root.right, list(path), pathSum + root.val)
            
            return self.answer
        
        return dfs(root, [], 0)