'''
https://leetcode.com/problems/remove-k-digits/

remove k digits from string to keep minimum output

A = 1axxx, B = 1bxxx, if the digits a > b, then A > B
num=425; k=1
    if we keep 4, then we get 42 or 45
    if we keep 2, then we get 25
iterate from the left to right on d1, d2, d3,...dn
    if d2 < d1, remove d1
    

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
        
        # or "0" is to address num="10" and k=2 i.e., leading 0
        return "".join(numStack).lstrip('0') or "0"


num = "1432219"
k = 3

# num = "10"
# k = 2

# num = "14"
# k = 2

s=Solution()
print(s.removeKdigits(num, k))
