'''



'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s=sorted(s)
        for i in range(1,len(s)):
            if s[i-1]!=s[i]:
                return i-1
        return -1
       
        
        
obj=Solution()
print(obj.firstUniqChar("loveleetcode"))
