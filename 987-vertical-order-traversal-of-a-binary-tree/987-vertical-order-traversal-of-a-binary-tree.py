# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        vertical = defaultdict(list)
        # traverse the tree using dfs (recursive function.)
        def dfs(root, row, col):
            if not root:
                return
            
            vertical[(row, col)].append(root.val)
            
            dfs(root.left, row+1, col-1)
            dfs(root.right, row+1, col+1)
            return
        
        # call the function
        dfs(root, 0, 0)
        
        # sort the values on the same row and column
        toSortVertical = vertical.items()
        listVertical = list(toSortVertical)
        listVertical.sort()
        
        vertical_col = defaultdict(list)
        for rows in listVertical:
            index = rows[0]
            values = rows[1]
            values.sort()
            vertical_col[index[1]].extend(values)
                    
        # sort the column and collect the answer.
        toSort = vertical_col.items()
        listToSort = list(toSort)
        listToSort.sort()
        
        Answer = []
        for tuples in listToSort:
            temp = tuples[1]
            Answer.append(temp)
        return Answer
    
    
    
    
    