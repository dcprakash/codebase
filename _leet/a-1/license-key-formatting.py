'''
https://leetcode.com/problems/fruit-into-baskets/  

'''

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        key_str = ("".join(s.split('-'))).upper()[::-1]
        res = ""
        for i in range(0, len(key_str), k):
            res += key_str[i:i+k] + "-"
        res = res[:len(res)-1]
        return res[::-1]

sol=Solution()
s = "5F3Z-2e-9-w"
k = 4
print(sol.licenseKeyFormatting(s,k))