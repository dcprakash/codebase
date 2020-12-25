# https://leetcode.com/problems/minimum-window-substring/solution/


def sub_string(s,t):
    if t in "".join(sorted(set(s))):
        return True
    else:
        return False


def min_window(s,t):
    n=len(s)
    mi=0
    r=[]
    for i in range(n):
        for j in range(i,n+1):
            if sub_string(s[i:j],t):
                mi=max(mi,j-i)
                r.append(mi)
    print(r)
            

s = "ADOBECODEBANC"
t = "ABC"
min_window(s,t)
