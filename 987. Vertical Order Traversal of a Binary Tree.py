# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        collect_col_row_val = []
        def dfs(root, row, col):
            if not root:
                return
            
            collect_col_row_val.append([col, row, root.val])
            
            dfs(root.left, row+1, col-1)
            dfs(root.right, row+1, col+1)
            return
        
        dfs(root, 0, 0)
        
        collect_col_row_val.sort()
        Answer = []
        i = 0
        while i < len(collect_col_row_val):
            temp = []
            temp.append(collect_col_row_val[i][2])
            prev = collect_col_row_val[i][0]
            i += 1
            while i < len(collect_col_row_val) and collect_col_row_val[i][0] == prev:
                temp.append(collect_col_row_val[i][2])
                i += 1
                
            Answer.append(temp)
                
        return Answer
