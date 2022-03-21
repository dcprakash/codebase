# https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
# remove repeating chars with least cost


class Solution:
    def minCost(self, s, cost):
        ans=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                ans+=min(cost[i],cost[i-1])
                # when it meet more than two consecutive same numbers
				# ex: a,a,a cost, 12,9,13 when it chose to delect 9 
				    # it should move 12 to number 9's position
                cost[i]=max(cost[i],cost[i-1])
        
        return ans


sol=Solution()        
s = "abaac"
cost = [1,2,3,4,5]
print(sol.minCost(s,cost))