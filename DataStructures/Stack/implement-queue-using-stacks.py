"""
https://leetcode.com/problems/implement-queue-using-stacks/

queue: FIFO
stack: LIFO

we will use stack, but implent queue
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]
        self.front=None
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack1:
            self.front=x
        self.stack1.append(x)
        
    
    # transfer s1 to s2, this way bottom of s1 will be on top of s2
    # do this only when s2 is empty, otherwise we will already have first in element to be first out ready in s2
    '''
    We have to remove element in front of the queue. This is the first inserted element in the stack s1 and it is 
    positioned at the bottom of the stack because of stack's LIFO (last in - first out) policy. 
    To remove the bottom element from s1, we have to pop all elements from s1 and to push them on to an additional stack s2, 
    which helps us to store the elements of s1 in reversed order. This way the bottom element of s1 will be positioned on 
    top of s2 and we can simply pop it from stack s2. Once s2 is empty, the algorithm transfer data from s1 to s2 again.
    '''
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        
    '''
    The front element is kept in constant memory and is modified when we push an element. 
    When s2 is not empty, front element is positioned on the top of s2
    '''
    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2:
            return self.stack2[-1]
        return self.front
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



