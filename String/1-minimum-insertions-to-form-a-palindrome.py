# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
# reverse given string
# n - longest commong substring(x,revers(x))


def lcs_util(x,y):
    m=n=len(x)
    l=[[0 for i in range(n + 1)] for j in range(m + 1)]
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
    

def lcs(x):
    return len(x)-lcs_util(x, x[::-1])

x="abcda"
print(lcs(x))
