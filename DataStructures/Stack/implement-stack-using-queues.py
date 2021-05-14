"""
Your module description
"""
from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1=deque()
        self.q2=deque()
        self.tops=None
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.appendleft(x)
        self.tops=x
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1)>1:
            self.tops=self.q1.pop()
            self.q2.appendleft(self.tops)
        res=self.q1.pop()
        temp=self.q1
        self.q1=self.q2
        self.q2=temp
        return res
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.tops
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1 and not self.q2
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.top())