'''
https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
https://leetcode.com/problems/palindromic-substrings/solution/
palindrome substrings
'''


def isPalindrome(s,lo,hi):
    while lo<hi:
        if s[lo]!=s[hi]:    return False
        lo+=1
        hi-=1
    return True


def countSubstrings(s,n):
    ans=0
    for lo in range(n):
        for hi in range(lo,n):
            ans+=isPalindrome(s,lo,hi)
    return ans


s="aaa"
print(countSubstrings(s,len(s)))

'''
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''