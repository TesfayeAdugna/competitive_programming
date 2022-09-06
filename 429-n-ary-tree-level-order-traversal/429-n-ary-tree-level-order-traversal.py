"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return
        level_order = []
        queue = deque([root])
        
        while queue:
            single_level = []
            for node in queue:
                single_level.append(node.val)
            level_order.append(single_level)
            
            for _ in range(len(queue)):
                temp = queue.popleft()
                for child in temp.children:
                    queue.append(child)
            
        return level_order