'''
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

Maximum Length of a Concatenated String with Unique Characters

bit manipulation to check duplicate characters
cbc = 212 in ascii terms
212 = 10 1 10
1<<2 i.e., 1<<10 is 100
1<<1       1<1 is 10
1<<2       1<10 is 100

100 & 10    is not > 0 so add -> 110
100 AND
 10
---
000


110 & 100   is > 0 so there is duplicate
110 AND
100
---
100 -> 4 which is >0

if there is duplicate, cur_bit & 1<<val will be 1
else    we add cur_bit and 1<<val


backtrack

https://www.youtube.com/watch?v=iGiTptPPUq8&ab_channel=HappyCoding
'''


class Solution:
    def maxLength(self, arr):
        
        # def hasduplicate(word):
        #     return len(set(word))!=len(word)
        
        # string has duplicate using bit
        def hasduplicate(word):
            cur_bit=0
            for i,s in enumerate(word):
                val=ord(s)-ord('a')
                if cur_bit & (1<<val) > 0:  return True
                cur_bit |= (1<<val)     # add to cur_bit value
            return False
            
        
        def backtrack(cur, ix):
            nonlocal ans
            ans=max(ans,len(cur))
            for i in range(ix,n):
                new=cur+arr[i]
                if not hasduplicate(new):
                    backtrack(new,i+1)
                #no need to replace backtrack orginal val, we used new string
            
        ans=0
        n=len(arr)
        backtrack("", 0)
        return ans


arr = ["un","iq","ue"]
s=Solution()
print(s.maxLength(arr))