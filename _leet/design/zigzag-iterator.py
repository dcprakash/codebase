"""
https://leetcode.com/problems/zigzag-iterator/solution/

The follow-up question is that what if we are given k vectors, instead of two?

for input of 2 vectors:
v1: [1,2]
v2: [3,4,5,6]
self.vectors=[[1, 2], [3, 4, 5, 6]]
self.queue=deque([(0, 0), (1, 0)])


"""
from collections import deque


class ZigzagIterator:
    def __init__(self, v1, v2):
        self.vectors = [v1, v2] #list of lists
        self.queue = deque()
        for index, vector in enumerate(self.vectors):
            # <index_of_vector, index_of_element_to_output>
            if len(vector) > 0:
                self.queue.append((index, 0))

    def next(self) -> int:
        if self.queue:
            vec_index, elem_index = self.queue.popleft()
            next_elem_index = elem_index + 1
            if next_elem_index < len(self.vectors[vec_index]):
                # append the pointer for the next round
                # if there are some elements left
                self.queue.append((vec_index, next_elem_index))

            return self.vectors[vec_index][elem_index]

        # no more element to output
        raise Exception


    def hasNext(self) -> bool:
        return len(self.queue) > 0
        
        
s=ZigzagIterator([1,2], [3,4,5,6])
for i in range(6):
    print(s.next())
print(s.hasNext())