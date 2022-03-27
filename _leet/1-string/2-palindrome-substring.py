'''
https://leetcode.com/problems/palindromic-substrings/solution/
palindrome substrings


Given a string, find the longest substring which is palindrome. 

'''


def isPalindrome(s,lo,hi):
    # print(s[lo:hi+1])
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
            # print(ans)
    return ans


s="aab"
print(countSubstrings(s,len(s)))

'''
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

There are two types of palindromes...

Odd and even length palindromes!

Odd-length palindromes have a single character in the middle. e.g. "civic" with middle character 'v'.

Even-length palindromes have two characters constitute the middle, both of which are same. 
e.g. "noon" with two middle characters 'o'.

Pop Quiz: Is "y" a palindrome? Is "gg" a palindrome?

Yes, both of the above are palindromes. "y" is single letter (hence odd-length) palindrome whose middle is the single 'y' character. 
"gg" is a double letter (hence even-length) palindrome whose middle is comprised of the two 'g' characters
'''