'''
https://leetcode.com/problems/remove-k-digits/

remove k digits from string to keep minimum output

Algorithm
    use stack
    iterate over num
    add each item to stack if item>top of stack
    remove item from stack if item<top of stack
        also decrement k
    

A = 1axxx, B = 1bxxx, if the digits a > b, then A > B
num=425; k=1
    if we keep 4, then we get 42 or 45
    if we keep 2, then we get 25
iterate from the left to right on d1, d2, d3,...dn
    if d2 < d1, remove d1
    
Given a non-negative integer num represented as a string, remove k digits from 
    the number so that the new number is the smallest possible.
    
arrange smallest
'''


class Solution:
    def removeKdigits(self, num, k):
        numStack=[]
        
        for digit in num:
            while k and numStack and numStack[-1]>digit:
                numStack.pop()
                k-=1
            
            numStack.append(digit)
            
        # list strip needed for num="14" and k=2
        # here we did not pop anything from stack and k is still 2
        numStack = numStack[:-k] if k else numStack
        
        # or "0" is to address num="14" and k=2
        return "".join(numStack).lstrip('0') or "0"


# num = "1432219"
# k = 3

# num = "10"
# k = 2

num = "14"
k = 2

# num = "9"
# k = 1

s=Solution()
print(s.removeKdigits(num, k))
