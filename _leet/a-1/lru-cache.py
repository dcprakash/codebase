'''
https://leetcode.com/problems/lru-cache/
https://www.youtube.com/watch?v=7v_mUfpg46E

use double linked list

'''
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1
        
    '''
    update operation is performed by removing the node from linked list, if key exist in dic (add new k:v node to tail)
    otherwise, create new node and add to the dic and linked list
    tail consist of LRU item; because we always add at tail (update removes node from middle of list and adding new node with key, value to tail)
    if dic reached capacity, then remove item from head
    '''
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
        
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    # insert "node" at end of linked list
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
      
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)