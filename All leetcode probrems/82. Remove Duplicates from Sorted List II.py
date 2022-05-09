"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        curr = head
        while head and head.next:
            if head.val == head.next.val or head.val -2000 == head.next.val:
                if head.val<=100:
                    head.val += 2000
                head.next.val += 2000
            head = head.next
                
        while curr and curr.val>100:
            curr = curr.next
            
        root = curr
        while curr and curr.next:
            if curr.next.val > 100:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return root
    