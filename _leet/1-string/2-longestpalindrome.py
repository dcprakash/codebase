'''
https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome#solution-5
https://leetcode.com/problems/longest-palindromic-substring/solution/


Given a string, find the longest substring which is palindrome. 
For example, 
Input: Given string :"forgeeksskeegfor", 
Output: "geeksskeeg"

sliding window
'''

def longestpalindrome(s):
    if s is "":
        return ""
    
    rev = s[::-1]
    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    max_len = 0
    max_end = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == rev[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > max_len:
                max_len = dp[i][j]
                max_end = i
            
    return s[max_end - max_len + 1: max_end + 1]

# s = "aaa"
s="forgeeksskeegfor"
#s="babad"
print(longestpalindrome(s))
