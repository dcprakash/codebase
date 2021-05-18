'''
https://leetcode.com/problems/paint-house/

paint house
steps
stairs
dynamic program
    
'''

class Solution:
    def minCost(self, costs):
        if not costs:   return 0
        n=len(costs)
        for i in range(1, n):
            costs[i][0]+=min(costs[i-1][1], costs[i-1][2])
            costs[i][1]+=min(costs[i-1][0], costs[i-1][2])
            costs[i][2]+=min(costs[i-1][0], costs[i-1][1])
            print(costs)
        return min(costs[n-1][0], costs[n-1][1], costs[n-1][2])

        
obj=Solution()
print(obj.minCost([[17,2,17],[16,16,5],[14,3,19]]))

