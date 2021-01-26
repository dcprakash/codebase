# https://leetcode.com/problems/reorder-list/
# https://leetcode.com/problems/reorder-list/submissions/

# reorder list alternatively
# get middle of list
# reverse second part of list
# rearragne list alternatively


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:    return
        
        # get middle of list
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # reverse second part of list
        prv, cur = None, slow
        while cur:
            cur.next, prv, cur = prv, cur, cur.next
        
        # rearragne list alternatively
        first, second = head, prv
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        