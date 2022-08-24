# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """
        example 1
        stack = []
        ex = [2, 1, 5]
        stack = [[2, 0], [1, 1]]
        stack = [[5, 2]]
        ans = [5, 5, 0]
        
        example 2
        stack = []
        ex = [2, 7, 4, 3, 5]
        stack = [[5,4]]
        
        ans = [7, 0, 5, 5, 0]
        """
        stack = []
        ans = []
        count = 0
        while head:
            ans.append(0)
            while stack and head.val > stack[-1][0]:
                temp = stack.pop()
                ans[temp[1]] = head.val
            stack.append([head.val, count])
            head = head.next
            count += 1
            
        return ans