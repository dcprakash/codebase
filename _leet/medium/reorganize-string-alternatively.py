# https://leetcode.com/problems/reorganize-string/solution/
# adjacent duplicates


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
        print(A[N/2:])
        print(A[:N/2])
        ans[::2], ans[1::2] = A[N/2:], A[:N/2]
        print(ans[::2])
        print(ans[1::2])
        return "".join(ans)

S = "aab"
s=Solution()
print(s.reorganizeString(S))


'''
# https://docs.python.org/release/2.3.5/whatsnew/section-slices.html

S = ['b','a','c']
L = range(10)

# print(S[0:2]) # subsrting from 0th index to 2nd (2nd not included)
# print(S[1:]) # 1 to end
# print(S[:1]) # up to 1


# print(S[1::2])
print(L[::1])
print(L[::2]) # nothing for 1st; jump by 2 in list of indices
print(L[::3])
L[1:2]=['a'] # replace list values; we can do bcz ist mutable
print(L)
'''