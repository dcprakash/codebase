# https://leetcode.com/problems/first-unique-number/


"""
Brute Force method
"""
from collections import deque

# class FirstUnique:

#     def __init__(self, nums: List[int]):
#         self.queue=deque(nums)

#     def showFirstUnique(self) -> int:
#         for item in self.queue:
#             if self.queue.count(item)==1:   return item
#         return -1

#     def add(self, value: int) -> None:
#         self.queue.append(value)
        

'''
keep a HashMap of numbers to booleans, where for each number that has been added, 
    we're storing the answer to the question is this number unique?. 
    We'll call it isUnique. Then, when FirstUnique.add(number) is called, one of three cases will apply:

This particular number has never been seen before now. Add it to isUnique with a value of true. Also, add it to the queue.
This particular number has already been seen by isUnique, with a value of true. 
    This means that the number was previously unique (and is currently in the queue), but with this new addition, it no longer is. 
    Update its value to false. Do not add it to the queue.
This particular number has already been seen by isUnique, with a value of false. 
    This means that it has already been seen twice before. We don't need to do anything, and shouldn't add it to the queue.

'''

class FirstUnique:

    def __init__(self, nums: List[int]):
        self._queue = deque()
        self._is_unique = {}
        for num in nums:
            # Notice that we're calling the "add" method of FirstUnique; not of the queue. 
            self.add(num)
        
    def showFirstUnique(self) -> int:
        # We need to start by "cleaning" the queue of any non-uniques at the start.
        # Note that we know that if a value is in the queue, then it is also in
        # is_unique, as the implementation of add() guarantees this.
        while self._queue and not self._is_unique[self._queue[0]]:
            self._queue.popleft()
        # Check if there is still a value left in the queue. There might be no uniques.
        if self._queue:
            return self._queue[0] # We don't want to actually *remove* the value.
        return -1
        
    def add(self, value: int) -> None:
        # Case 1: We need to add the number to the queue and mark it as unique. 
        if value not in self._is_unique:
            # print(self._queue)
            self._is_unique[value] = True
            self._queue.append(value)
            # print(self._queue)
        # Case 2 and 3: We need to mark the number as no longer unique.
        else:
            self._is_unique[value] = False