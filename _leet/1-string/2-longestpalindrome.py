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
                if i-dp[i][j]+1 == len(s)-1-j:  #if all chars are accounted for with palnifrom in place with maxlen
                    max_len = dp[i][j]
                    max_end = i
    print(dp)
            
    return s[max_end - max_len + 1: max_end + 1]

# s = "aaa"
# s="forgeeksskeegfor"
s="babd"
print(longestpalindrome(s))

'''
   d b a b
   
b  0 1 0 1  (i=0, j=3) 0-1+1==4-1-3
a
b
d
   
[[0, 1, 0, 1], 
 [0, 0, 2, 0], 
 [0, 1, 0, 3], 
 [1, 0, 0, 0]]

'''