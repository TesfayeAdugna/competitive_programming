# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        newlist = []
        
        while head:
            newlist.append(head.val)
            head = head.next
            
        newlist = sorted(newlist)
        
        head = node
        for i in range(len(newlist)):
            node.val = newlist[i]
            node = node.next
            
        return head