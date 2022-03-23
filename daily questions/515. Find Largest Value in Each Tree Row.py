"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        if not root:
            return output
        queue = deque()
        queue.append(root)
        
        while queue:
            curr_max = queue[0].val
            for ele in queue:
                if ele.val > curr_max:
                    curr_max = ele.val
            output.append(curr_max)
            
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.right:
                    queue.append(temp.right)
                if temp.left:
                    queue.append(temp.left)
                
        return output
                
                