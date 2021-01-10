# https://leetcode.com/problems/generate-parentheses/solution/

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

s=Solution()
print(s.generateParenthesis(3))


'''
l=1	(

l=2	(

l=3	(
	s=(((
	l=3

	r=1	)
	r=2	)
	r=3	)
		s=((()))
		l=r=3
	ans.append(s)
	return

	l=2, r=1
		(()

		l=3, r=1
			(()(

		l=3, r=2
			(()()

		l=3, r=3
			(()())
'''