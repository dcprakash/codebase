"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

Recall that odd numbers always have a last bit of 1. 
Subtracting 1, from an odd number, changes the last bit from 1 to 0.

Dividing by 2 removes the last bit from the number.

"""

class Solution:
    def numberOfSteps (self, num):
        bits=bin(num)[2:]
        steps=0
        for b in bits:
            if b=="1":  steps+=2
            else:   steps+=1
        return steps-1
        
        
s=Solution()
num=14
print(s.numberOfSteps(num))