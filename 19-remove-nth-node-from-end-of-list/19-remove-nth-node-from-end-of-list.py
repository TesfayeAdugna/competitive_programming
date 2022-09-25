# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        length = 0
        while head:
            length+=1
            head = head.next
            
        rem = length - n
        if length<=1 and rem==0:
            return None
        i = 0
        head = node
        while i<rem-1:
            node = node.next
            i+=1
            
        if n == length:
            return head.next
        if node.next:
            node.next = node.next.next
        
        return head