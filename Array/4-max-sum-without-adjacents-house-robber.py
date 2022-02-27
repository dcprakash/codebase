"""
https://leetcode.com/problems/house-robber

max sum without adjacent
max sum without alternate
dynamic program

nums = [2,7,9,3,1]

rob_next=1 (Start from last element)
rob_next_plus_one=0 (no element after last element so 0)
current = max(1, 0 + 3)=3
rob_next_plus_one=1
rob_next=3

current = max(3, 9 + 1)=10
rob_next_plus_one=3
rob_next=10

current = max(10, 3 + 7)=10
rob_next_plus_one=10
rob_next=10

current = max(10, 10 + 2)=12
rob_next_plus_one=10
rob_next=12

return 12


- We will make use of two variables here called robNext and robNextPlusOne which at any point will represent the optimal solution for maxRobbedAmount[i + 1] and maxRobbedAmount[i + 2]. These are the two values that we need to calculate the current value.
- We set robNextPlusOne to 0 since this means the robber doesn't have any houses left to rob, thus zero profit. Additionally, we set robNext to nums[N - 1] because in this case there is only one house to rob which is the last house. Robbing it will yield the maximum profit.
     Note We are assuming that robNextPlusOne is the value of maxRobbedAmount[N] and robNext is maxRobbedAmount[N-1] initially.
- We iterate from N - 2 down to 0 and set current = max(robNext, robNextPlusOne + nums[i]). Note that this is the same as the dynamic programming solution except that we are making use of our variables and not entries from the table.
- Set robNextPlusOne = robNext.
- Set robNext = current. Updating the two variables is important as we iterate down to 0.
- We return the value in robNext.

"""
# class Solution:
#     def rob(self, nums):
#         incl=0
#         excl=0
#         for i in nums:
#             new_excl=max(incl, excl)
#             incl=excl+i
#             excl=new_excl
#         return max(incl, excl)
        
class Solution2:
    
    def rob(self, nums):
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        N = len(nums)
        
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])
            
            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current
            
        return rob_next
    

# obj=Solution()
# print(obj.rob([2,7,9,3,1]))

obj2=Solution2()
print(obj2.rob([2,7,9,3,1]))