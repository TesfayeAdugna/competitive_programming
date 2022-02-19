"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return list1
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        
        tempo = list1
        while list1:
            if list1.next is None:
                list1.next = list2
                break
            else:
                list1 = list1.next
                
        list1 = tempo
        newlist = []
        while list1:
            newlist.append(list1.val)
            list1 = list1.next
        
        newlist = sorted(newlist)
        
        list1 = tempo
        for i in range(len(newlist)):
            list1.val = newlist[i]
            if i == 0:
                tem = list1
            list1 = list1.next
        
        list1 = tem
        return list1