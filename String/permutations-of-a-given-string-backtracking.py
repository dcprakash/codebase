# https://leetcode.com/problems/permutations/
# string permutations, permute, backtracking

'''
https://leetcode.com/problems/permutations/solution/ 
Iterate over the integers from index first to index n - 1.
    Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
    Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
    Now backtrack, i.e. swap(nums[first], nums[i]) back.

'''

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
