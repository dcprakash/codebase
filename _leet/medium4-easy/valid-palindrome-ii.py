"""
https://leetcode.com/problems/valid-palindrome-ii
valid palindrome after removal of one character

"""

class Solution(object):
    def validPalindromeEasy(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            temp=s[:i]+s[i+1:]
            if temp==temp[::-1]:    return True
        
        return s==s[::-1]
        
    
    # below method does not work yet
    def validPalindrome(self, s):
        def isPalindrome(string, low, high):
            while low<high:
                if string[low]!=string[high]:   return False
                low+=1
                high-=1
            return True
        
        l=0
        h=len(s)-1
        while l<h:
            if s[l]==s[h]:
                l+=1
                h-=1
            elif h<len(s):
                temp=s[:h]+s[h+1:]
                if temp==temp[::-1]:    return True
            elif l<h:
                temp=s[:l]+s[l+1:]
                if temp==temp[::-1]:    return True
            
                # if isPalindrome(s, l+1, h): return True
                # if isPalindrome(s, l, h+1): return True
        return True
            
