# https://leetcode.com/problems/sort-list/submissions/
# sort linked list

# Definition for singly-linked list.

'''
class Solution:
  def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    queue = []
    
    while head:
      queue.append(head.val)
      head = head.next
      
    queue.sort(reverse=True);
    
    dummy = ListNode();
    pointer = dummy
    
    while len(queue) > 0:
      val = queue.pop();
      pointer.next = ListNode(val)
      pointer = pointer.next
      
    return dummy.next
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = head
        advance_slower = False
        slower = head
        fast = head
        
        while fast is not None:
            if advance_slower:
                slower = slower.next
            advance_slower = True
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        slower.next = None

        left = self.sortList(head)

        right = self.sortList(slow)

        current = None
        result = None
        while left and right:
            if left.val <= right.val:
                if current:
                    current.next = ListNode(left.val)
                    current = current.next
                else:
                    current = ListNode(left.val)
                left = left.next
            else:
                if current:
                    current.next = ListNode(right.val)
                    current = current.next
                else:
                    current = ListNode(right.val)
                right = right.next
            if result is None:
                result = current

        if left is not None:
            current.next = left
        else:
            current.next = right

        return result
                
            