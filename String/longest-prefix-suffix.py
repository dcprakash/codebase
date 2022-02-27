# https://www.geeksforgeeks.org/longest-prefix-also-suffix/
#2: remove first 2
#012345678
#aabcdaabc
# longest prefix suffix
'''
Given a string s, find the length of the longest prefix, which is also a suffix. 
The prefix and suffix should not overlap.

Input : aabcdaabc
Output : 4
The string "aabc" is the longest
prefix which is also suffix.

'''

def longestPrefixSuffix(s):
    n=len(s)
    for res in range(n//2, 0, -1): #start, stop, step
        t1=s[0:res]
        t2=s[n-res:n]
        if t1==t2:
            return res
    return 0


s="abcdaabc"
print(longestPrefixSuffix(s))

