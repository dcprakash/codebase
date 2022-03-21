"""
https://www.youtube.com/watch?v=OM1MTokvxs4&ab_channel=NeetCode
https://leetcode.com/problems/triangle/
minimum path sum triangle
"""


class Solution:
    def minimumTotal(self, triangle):
        dp=[0]*(len(triangle[-1])+1)  # last row is longest in triangle
        for row in triangle[::-1]:
            print(dp)
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1]) # overwrite original values
        
        return dp[0]
            

# triangle = [[2],[3,4],[6,5,9],[4,10,8,3]]
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
s=Solution()
print(s.minimumTotal(triangle))