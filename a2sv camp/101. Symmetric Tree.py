"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        
        def bfs(leftnode,rightnode):
            if not leftnode or not rightnode:
                return leftnode == rightnode
            
            if leftnode.val != rightnode.val:
                return False
            
            return bfs(leftnode.left, rightnode.right) and bfs(leftnode.right,rightnode.left)
        
        
        return bfs(root.left,root.right)
        
        