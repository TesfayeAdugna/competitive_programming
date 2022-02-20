"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        newlist = []
        
        node = head
        while head:
            newlist.append(head.val)
            head= head.next
            
        head = node
        for i in range(len(newlist)//2):
            node.val = newlist[i]
            node.next.val = newlist[-i-1]
            
            if i == len(newlist)//2-1:
                break
                
            node = node.next.next
            
            
        if len(newlist)>2 and len(newlist)%2 == 1:
            node.next.next.val = newlist[len(newlist)//2]
            
            