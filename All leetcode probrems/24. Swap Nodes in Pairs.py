"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 
Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            x = head.val
            y = head.next.val
            head.val = y
            head.next.val = x
            return head
            
        
        result = head
        while head:
            temp = head.val
            tempo = head.next.val
            head.val = tempo
            head.next.val = temp
            if head.next.next is None:
                break
            elif head.next.next.next is not None:
                head = head.next.next
            else:
                break
            
        head = result
        return head
        
        
        