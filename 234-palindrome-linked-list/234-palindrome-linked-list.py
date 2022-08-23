# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        root = head
        root2 = head
        root3 = head
        length = 0
        while root:
            length += 1
            root = root.next
            
        half_lst = []
        for i in range((length+1)//2):
            half_lst.append(root2.val)
            root2 = root2.next
            
        half_lst = half_lst[::-1]
        j = 0
        i = 0
        flag = True
        while root3:
            if i >= length//2:
                if root3.val == half_lst[j]:
                    j += 1
                    root3 = root3.next
                else:
                    flag = False
                    break
            else:
                root3 = root3.next
                
            i += 1
            
        return flag