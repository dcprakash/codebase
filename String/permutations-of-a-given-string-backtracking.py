# https://leetcode.com/problems/permutations/
# string permutations, permute, backtracking


class Solution:
    def permute(self, nums):
        
        def backtrack(first = 0):
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output


nums = [1,2,3]
s=Solution()
print(s.permute(nums))
