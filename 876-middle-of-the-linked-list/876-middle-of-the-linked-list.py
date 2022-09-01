# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 0
        root = head
        while root:
            length += 1
            root = root.next
        i = 0
        while head and i < length//2:
            head = head.next
            i += 1
            
        return head