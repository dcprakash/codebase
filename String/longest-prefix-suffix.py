# https://www.geeksforgeeks.org/longest-prefix-also-suffix/
#2: remove first 2
#012345678
#aabcdaabc
s="aabcdaabc"
n=len(s)
for res in range(n//2, 0, -1): #start, stop, step
    p=s[:res]
    s=s[n-res:n]
    if p==s:
        print(len(p))