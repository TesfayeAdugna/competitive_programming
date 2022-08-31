# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def dfs(parent, head):
            if not head:
                return parent
            
            par = dfs(head, head.next)
            head.next = parent
            return par
        
        return dfs(None, head)