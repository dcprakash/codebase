
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

# ABC
# AGB

#     a g b  y
#     0 0 0  ^
# a 0 1 1 1  |
# b 0 1 1 2  |
# c 0 1 1 2  |
#            j
# x - - - - > i

def lcs(x,y):
    m=len(x)
    n=len(y)
    
    l=[[None]*(n+1) for i in range(m+1)]
    # print(l)
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    return l[m][n]


# X = "AGGTAB"
# Y = "GXTXAYB"
X = "ABC"
Y = "AGB"
print("Length of LCS is ", lcs(X, Y))
