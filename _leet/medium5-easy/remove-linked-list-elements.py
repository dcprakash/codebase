"""
https://leetcode.com/problems/remove-linked-list-elements

linked list
linkedlist

remove node from linked list
delete node from linked list


"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel=ListNode(0)
        sentinel.next=head
        
        prv, cur = sentinel, head
        while cur:
            if cur.val==val:
                prv.next=cur.next
            else:
                prv=cur
            cur=cur.next
        
        return sentinel.next
        