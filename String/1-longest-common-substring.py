
# https://www.geeksforgeeks.org/longest-common-substring-dp-29/

#   e e k s G e
# G 0 0 0 0 1 0
# e 1 1 0 0 0 2		r=2
# e 1 2 0 0 0 1
# k 0 0 3 0 0 0		r=3
# s 0 0 0 4 0 0		r=4
# result = max(result, LCSuff[i][j])
# result = 4


def lcs(x,y):
    m=len(x)
    n=len(y)
    result=0
    l=[[None]*(n+1) for i in range(m+1)]
    # print(l)
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=l[i-1][j-1]+1
                result=max(result,l[i][j])
            else:
                l[i][j]=0
    return result



X = "abcde"
Y = "ace"

# X = "GeeksforGeeks"
# Y = "GeeksQuiz"
# X = "abcda"
# Y = "adcba"
print("Length of LCS is ", lcs(X, Y))

