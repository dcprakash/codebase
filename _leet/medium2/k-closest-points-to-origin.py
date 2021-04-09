"""
https://leetcode.com/problems/k-closest-points-to-origin/solution/

"""
class Solution:
    def kClosest(self, points, K):
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:K]
        
s=Solution()
points=[[3,3],[5,-1],[-2,4]]
k=2
print(s.kClosest(points,k))
        