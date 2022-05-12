# https://leetcode.com/problems/sort-list/submissions/
# sort linked list
# https://www.youtube.com/watch?v=TGveA1oFhrc&ab_channel=NeetCode
# Definition for singly-linked list.

'''
merge sort
mergesort
_leet/medium8/merge-sort.py
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        left = head
        right = self.getmid(head)
        temp=right.next
        right.next=None
        right=temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    
    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if list1:   tail.next=list1
        if list2:   tail.next=list2
        return dummy.next
    
    
    def getmid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
