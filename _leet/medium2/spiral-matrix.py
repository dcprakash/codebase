'''
https://leetcode.com/problems/spiral-matrix/
print matrix in sprial order
'''

class Solution:
    def generateMatrix(self, n):

        def spiral_coords(top, left, bottom, right):
            for c in range(left, right + 1):
                yield top, c
            for r in range(top + 1, bottom + 1):
                yield r, right
            if top < bottom and left < right:
                for c in range(right - 1, left, -1):
                    yield bottom, c
                for r in range(bottom, top, -1):
                    yield r, left

        if not n: return []
        ans = [[0]*n for _ in range(n)]

        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        while top <= bottom and left <= right:
            for r, c in spiral_coords(top, left, bottom, right):
                ans[r][c] = num
                num += 1
            top += 1; bottom -= 1
            left += 1; right -= 1
            
        return ans


n=3
s=Solution()
print(s.generateMatrix(n))
