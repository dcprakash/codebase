'''
https://leetcode.com/problems/first-unique-character-in-a-string

First unique character in string

duplicate string
duplicate character
'''

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for ix, ch in enumerate(s):
            if count[ch]==1:
                return ix
        return -1
       
        
        
obj=Solution()
print(obj.firstUniqChar("loveleetcode"))
