# https://leetcode.com/problems/reorganize-string/solution/
# adjacent duplicates
# string slices, string partition


class Solution(object):
    def reorganizeString(self, S):
        N = len(S)
        A = []
        # print(S.count('a'), 'a')
        # get result like [(1,'b'),(2,'a')]
        for c, x in sorted((S.count(x), x) for x in set(S)):
            # if there are aaab, then more than half len of char is a
            # we cannot arrange alternatively
            if c > (N+1)/2: return ""
            A.extend(c * x)
        ans = [None] * N
        # print(A[N/2:])    #from ith index to n
        # print(A[:N/2])    #upto ith index
        ans[::2], ans[1::2] = A[N/2:], A[:N/2]
        # print(ans[::2])   #alternate starting from 0th index
        # print(ans[1::2])  #alternate starting from 1st index
        return "".join(ans)

S = "aab"
s=Solution()
print(s.reorganizeString(S))


'''
# https://docs.python.org/release/2.3.5/whatsnew/section-slices.html

string = ['b','a','c', 'd']
L = range(10)

print(string[0:2]) # subsrting from 0th index to 2nd (2nd not included)
print(string[1:]) # 1 to end
print(string[:1]) # up to 1


print(string[::2])  #alternate starting from 0th index
print(string[1::2]) #alternate starting from 1st index
print(L[::1])
print(L[::2]) # nothing for 1st; jump by 2 in list of indices
print(L[::3])
# L[1:2]=['a'] # replace list values; we can do bcz ist mutable
print(L)
'''