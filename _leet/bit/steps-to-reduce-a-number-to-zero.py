"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

Recall that odd numbers always have a last bit of 1. 
Subtracting 1, from an odd number, changes the last bit from 1 to 0.

Dividing by 2 removes the last bit from the number.

"""

class Solution:
    def numberOfStepsBit (self, num):
        bits=bin(num)[2:]
        steps=0
        for b in bits:
            if b=="1":  steps+=2
            else:   steps+=1
        return steps-1
            
    def numberOfSteps (self, num):
        steps = 0 # We need to keep track of how many steps this takes.
        while num > 0: # Remember, we're taking steps until num is 0.
            if num % 2 == 0: # Modulus operator tells us num is *even*.
                num = num // 2 # So we divide num by 2.
            else: # Otherwise, num must be *odd*.
                num = num - 1 # So we subtract 1 from num.
            steps = steps + 1 # We *always* increment steps by 1.
        return steps # And at the end, the answer is in steps so we return it.
        
s=Solution()
num=14
print(s.numberOfSteps(num))