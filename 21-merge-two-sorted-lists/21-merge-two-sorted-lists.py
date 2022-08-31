# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = None
        if list1 or list2:
            head = ListNode()
            root = head
        
        while list1 or list2:
            if not list1:
                while list2:
                    head.val = list2.val
                    list2 = list2.next
                    if list2:
                        head.next = ListNode()
                        head = head.next                
                break
            if not list2:
                while list1:
                    head.val = list1.val
                    list1 = list1.next
                    if list1:
                        head.next = ListNode()
                        head = head.next
                break
            
            if list1.val <= list2.val:
                head.val = list1.val
                list1 = list1.next
                if list1 or list2:
                    head.next = ListNode()
                    head = head.next
            else:
                head.val = list2.val
                list2 = list2.next
                if list1 or list2:
                    head.next = ListNode()
                    head = head.next
                
        return root
    
    
    
    
    
    
    