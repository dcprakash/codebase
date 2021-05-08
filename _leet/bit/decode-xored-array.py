"""
https://leetcode.com/problems/decode-xored-array/
XOR
"""
class Solution:
    def decode(self, encoded, first):
        res=[first]
        for i in encoded:
            res.append(i ^ res[-1])
        return res
        

s=Solution()
encoded = [1,2,3]
first = 1
print(s.decode(encoded,first))