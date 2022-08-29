# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newlist = []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                heapq.heappush(newlist,head.val)
                head = head.next
        
        if len(newlist)<1:
            return None
        node = ListNode()
        noder = node

        while len(newlist)>0:
            node.val = newlist[0]
            if len(newlist) <=1:
                break
            node.next = ListNode()
            node = node.next
            
            heapq.heappop(newlist)
            
        return noder