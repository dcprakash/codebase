# https://www.geeksforgeeks.org/longest-prefix-also-suffix/
#2: remove first 2
#012345678
#aabcdaabc

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

