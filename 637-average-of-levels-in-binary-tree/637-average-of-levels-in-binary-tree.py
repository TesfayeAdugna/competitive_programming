# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        Answer = []
        queue = deque([root])
        
        while queue:
            
            temp_sum = 0
            for i in range(len(queue)):
                temp_sum += queue[i].val
                
            temp_avr = temp_sum/len(queue)
            Answer.append(temp_avr)
            
            for _ in range(len(queue)):
                child = queue.popleft()
                if child.left:
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)
                
        return Answer
    
    
    
    
    