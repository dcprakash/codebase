# https://leetcode.com/problems/middle-of-the-linked-list/submissions/
# middle of linked list
# center of linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        