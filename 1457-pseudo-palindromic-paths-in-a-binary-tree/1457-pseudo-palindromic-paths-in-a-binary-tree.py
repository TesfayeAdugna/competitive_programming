# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def isPalindrome(string):
            count = 0
            for val in string:
                if string[val]%2 == 1:
                    count += 1
            return count <= 1
        
        def dfs(root, path):
            left = 0
            right = 0
            if root.val in path:
                path[root.val] += 1
            else:
                path[root.val] = 1
                
            if not root.left and not root.right:
                return 1 if isPalindrome(path) else 0
            if root.left:
                left = dfs(root.left, dict(path))
            if root.right:
                right = dfs(root.right, dict(path))
            
            return left + right
        
        return dfs(root, {})
    
    
    
    
    
    
    
    
    
            