"""
https://leetcode.com/problems/palindrome-linked-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # copy linked list to array and validate array
    def isPalindromeEasy(self, head: ListNode) -> bool:
        val=[]
        cur=head
        while cur is not None:
            val.append(cur.val)
            cur=cur.next
        return val==val[::-1]
        
        
    
    '''
    Find the end of the first half.
    Reverse the second half.
    Determine whether or not there is a palindrome.
    Restore the list.
    Return the result.
    '''
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # by this point, 1->2->2->1 will become 1->2->1->2

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result    
        

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while slow.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous, current = None, head
        while current:
            current.next, previous, current = previous, current, current.next
        return previous