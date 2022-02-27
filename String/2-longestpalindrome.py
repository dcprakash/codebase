'''
https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
https://leetcode.com/problems/palindromic-substrings/solution/ (similar)

Given a string, find the longest substring which is palindrome. 
For example, 
Input: Given string :"forgeeksskeegfor", 
Output: "geeksskeeg"
'''

def longestpalindrome(s):
    n=len(s)
    max_len=1
    start=0
    for i in range(1,n):
        l=i-1
        h=i
            
        while l>=0 and h<n and s[l]==s[h]:
            if h-l+1>max_len:
                max_len=h-l+1
                start=l
            l-=1
            h+=1

    res=""
    for i in range(start,start+max_len):
        res+=s[i]
    return res

# s = "aaa"
s="forgeeksskeegfor"
print(longestpalindrome(s))
