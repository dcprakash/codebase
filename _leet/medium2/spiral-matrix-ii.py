'''
https://leetcode.com/problems/spiral-matrix-ii/
https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
'''

class Solution:
    def generateMatrix(self, n):

        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not n: return []
        ans = [[0]*n for _ in range(n)]

        r1, r2 = 0, n - 1
        c1, c2 = 0, n - 1
        num = 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans[r][c] = num
                num += 1
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
            
        return ans


n=3
s=Solution()
print(s.generateMatrix(n))
