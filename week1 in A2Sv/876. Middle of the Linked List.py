"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #to know the length of the linkedlist
        count = 1
        temp = head
        while temp.next is not None:
            temp = temp.next
            count+=1
            
        #to return the middle
        middle = count//2 + 1
        counts = 1
        current = head
        if middle <= 2:
            if middle == 1:
                return current
            elif middle == 2:
                return current.next
        
        while current.next is not None:
            if counts < middle:
                current = current.next
                counts += 1
            else:
                counts+=1
                return current
