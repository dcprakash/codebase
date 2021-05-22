"""
https://leetcode.com/problems/moving-average-from-data-stream

data stream average
moving average of data stream
average of stream

"""
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size=size
        self.queue=collections.deque()
        self.windowsum=0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        tail = self.queue.popleft() if len(self.queue) > self.size else 0
        self.windowsum = self.windowsum - tail + val
        return self.windowsum / min(len(self.queue), self.size)
        
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)