"""
https://leetcode.com/problems/max-stack/
"""

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main=[]
        self.max=[]
        

    def push(self, x: int) -> None:
        # print(self.main)
        # print(self.max)
        self.main.append(x)
        if not self.max or self.max[-1]<=x:
            self.max.append(x)
        

    def pop(self) -> int:
        # print(self.main)
        # print(self.max)
        if self.max[-1]==self.main[-1]:
            self.max.pop()
        return self.main.pop()
        

    def top(self) -> int:
        # print(self.main)
        # print(self.max)
        return self.main[-1]
        

    def peekMax(self) -> int:
        # print(self.main)
        # print(self.max)
        return self.max[-1]
        

    def popMax(self) -> int:
        # For popMax, we know what the current maximum (peekMax) is. 
        # We can pop until we find that maximum, then push the popped elements back on the stack.
        max_ele=self.max[-1]
        temp=[]
        while self.main and self.main[-1]!=max_ele:
            temp.append(self.main.pop())
        if self.main[-1]==max_ele:
            self.main.pop()
            self.max.pop()
        self.main+=temp
        # print(self.main)
        # print(self.max)
        return max_ele


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()