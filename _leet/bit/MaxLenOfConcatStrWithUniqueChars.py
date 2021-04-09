'''

Maximum Length of a Concatenated String with Unique Characters

bit manipulation to check duplicate characters
cbc = 212 in ascii terms
212 = 10 1 10
1<<2 i.e., 1<<10 is 100

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
                cur_bit |= (1<<val)
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