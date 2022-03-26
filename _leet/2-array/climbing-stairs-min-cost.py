'''
https://leetcode.com/problems/min-cost-climbing-stairs/

https://www.youtube.com/watch?v=OoGswqFU-zs&ab_channel=NickWhite

climbing stairs
climb stairs
steps

dynamic program
'''

class Solution:
    def minCostClimbingStairs(self, cost):
        for i in range(2, len(cost)):
            cost[i]+=min(cost[i-2], cost[i-1])
        # print(cost)    # [1, 100, 2, 3, 3, 103, 4, 5, 104, 6]
        return min(cost[len(cost)-2], cost[len(cost)-1])
        
        
    # if we are asked not to modify original array
    # we can use dynamic programming techniques
    def minCostClimbingStairsDynamic(self, cost):
        step1=0
        step2=0
        for i in range(len(cost)-1, -1, -1):
            current_step=cost[i]+min(step1, step2)
            step1=step2
            step2=current_step
        return min(step1, step2)
        
        
obj=Solution()
print(obj.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(obj.minCostClimbingStairsDynamic([1,100,1,1,1,100,1,1,100,1]))

