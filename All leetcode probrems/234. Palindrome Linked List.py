"""
https://leetcode.com/problems/palindrome-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
                
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
            
        length = len(lst)
        newlen = length//2
        lst1 = lst[:newlen]
        if length%2==1:
            lst2 = lst[newlen+1:]
        else:
            lst2 = lst[newlen:]
        return lst1 == lst2[::-1]