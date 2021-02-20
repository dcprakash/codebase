
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
    # print(l)
    return l[m][n]


X = "GeeksforGeeks"
Y = "GeeksQuiz"
# X = "ABC"
# Y = "AGB"
print("Length of LCS is ", lcs(X, Y))


'''
[        G  e  e. k. s. Q. u. i. z
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
g    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
e    [0, 1, 2, 2, 2, 2, 2, 2, 2, 2], 
e    [0, 1, 2, 3, 3, 3, 3, 3, 3, 3], 
k    [0, 1, 2, 3, 4, 4, 4, 4, 4, 4], 
s    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5], 
f    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5], 
o    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5], 
r    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5], 
g    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5], 
e    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5], 
e    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5], 
k    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5], 
s    [0, 1, 2, 3, 4, 5, 5, 5, 5, 5]
]
'''