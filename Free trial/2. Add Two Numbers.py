"""
https://leetcode.com/problems/add-two-numbers/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = 1
        num1 = 0
        num2 = 0
        while l1:
            num1 += l1.val * temp
            temp *= 10
            l1 = l1.next
        temp = 1
        while l2:
            num2 += l2.val * temp
            temp *=10
            l2 = l2.next
            
        summ = num1 + num2
        node = ListNode()
        root = node
        while summ > 0:
            node.val = summ%10
            summ = summ//10
            if summ>0:
                node.next = ListNode()
                node = node.next
            
        return root
        
        
        
        
        