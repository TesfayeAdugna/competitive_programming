# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
            
        root = None
        if stack:
            node = ListNode()
            root = node
        while stack:
            node.val = stack.pop()
            if stack:
                node.next = ListNode()
                node = node.next
            
        return root