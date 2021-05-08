"""
https://leetcode.com/problems/design-hashmap/

loop and condition: https://www.tutorialspoint.com/python3/python_while_loop.htm

Each type of list has the normal advantages/disadvantages: 
a regular list has O(1) lookup time but O(M) remove time, 
while a linked list has O(M) lookup time but O(1) remove time 
(where M is the number of items in the bucket).

"""

class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.val = None
        self.next = None
        
class MyHashMap:
    SIZE = 1000

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashing = [ListNode(-1) for _ in range(self.SIZE)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        head = self.hashing[key % self.SIZE]
        current = head.next
        # itereate cur.nxt until key is found, if found then break loop and update that cur.val
        # if no more cur.nxt left and key not found; add item at end; update cur.val
        while current:
            if current.key==key:    break
            current=current.next
        else:
            current=ListNode(key)
            current.next=head.next
            head.next=current
        current.val=value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        current=self.hashing[key % self.SIZE].next
        while current:
            if current.key==key:    break
            current = current.next
        else:
            return -1
        return current.val
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        current=self.hashing[key % self.SIZE]
        while current and current.next:
            if current.next.key==key:   break
            current=current.next
        else:
            return None
        current.next = current.next.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
