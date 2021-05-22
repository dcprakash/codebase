"""
https://leetcode.com/problems/palindrome-number/
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if s[0]=='-':   return False
        return s==s[::-1]
        
obj=Solution()
print(obj.isPalindrome(-121))
print(obj.isPalindrome(121))