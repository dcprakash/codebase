class Solution:
    def all_unique(self, str2):
        return len(set(str2))==len(str2)
        
        # # res=""
        # res=set()
        # for i in str2:
        #     if i in res:
        #         return False
        #     else:
        #         #res+=i
        #         res.add(i)
        # return True
    

    def lengthOfLongestSubstring(self, s):
        ans=0
        n=len(s)
        if ' ' in s:
            return 1
        for i in range(n):
            for j in range(n+1):
                if self.all_unique(s[i:j]):
                    ans=max(ans,j-i)
        return ans


s=Solution()
string="geeksforgeeks"
print(s.lengthOfLongestSubstring(string))
