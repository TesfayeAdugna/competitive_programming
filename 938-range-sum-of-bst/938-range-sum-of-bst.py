# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        # dfs approach
#         self.Total_sum = 0
#         def dfs(root):
#             if root.val >= low and root.val <= high:
#                 self.Total_sum += root.val
                
#             if root.left:
#                 dfs(root.left)
#             if root.right:
#                 dfs(root.right)
            
#             return self.Total_sum
        
#         return dfs(root)
    
        # bfs approach
        Total_sum = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                temp = q.popleft()
                if temp.val >= low and temp.val <= high:
                    Total_sum += temp.val
                    
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                
        return Total_sum
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
