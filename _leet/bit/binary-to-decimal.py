"""
bit manipulation

https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/solution/

2^3 2^2 2^1 2^0
8   4   2   1
0   0   1   1   3
0   1   0   1   5

convert 101 into 1*2^2 + 0*2^1 + 1*2^0 = 5

"""

class Solution:
    def getDecimalValue(self, head):
        num=head[0]
        for i in range(1,len(head)):
            print(num<<1)
            num=(num<<1) | head[i]  # multiply by 2 and add current value
            print(num)
        return num
        
        
        
s=Solution()
head=[1,0,1]
print(s.getDecimalValue(head))
