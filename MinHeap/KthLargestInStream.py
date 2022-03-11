"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""

from heapq import (
    heapify,
    heappush,
    heappop,
    heappushpop
)

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
        


# ["KthLargest","add","add","add","add","add"]
# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
k=3
nums=[4,5,8,2]
obj = KthLargest(k, nums)
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))