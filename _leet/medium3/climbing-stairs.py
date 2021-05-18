'''
https://leetcode.com/problems/climbing-stairs

https://www.youtube.com/watch?v=uHAToNgAPaM&ab_channel=KevinNaughtonJr.

We have 2 ways to climb stairs:
    1 step at a time
    2 steps at a time

We can climb 0 steps in 1 way
1 step in 1 way
2 step in :
    1 + 1
    2
3 steps in:
    1+1+1
    1+2
    2+1
    
climb stairs
steps

dynamic program
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:    return 1
        dp=[None for _ in range(n+1)]
        dp[0]=1
        dp[1]=1
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        
        
obj=Solution()
print(obj.climbStairs(8))

