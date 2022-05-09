"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        stack = []
        node = head
        ans = node
        while head:
            for i in range(k):
                if head:
                    stack.append(head.val)
                    head = head.next
            if len(stack)==k:
                while stack:
                    node.val = stack.pop()
                    node = node.next
            else:
                for i in range(len(stack)):
                    node.val = stack[i]
                    node = node.next
                
        return ans  