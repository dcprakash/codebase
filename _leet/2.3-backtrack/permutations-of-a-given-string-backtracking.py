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
        
        def backtrack(start = 0):
            if start == n:  
                res.append(nums[:])
            for i in range(start, n):
                # place i-th integer first 
                # in the current permutation
                nums[start], nums[i] = nums[i], nums[start]
                # use next integers to complete the permutations
                backtrack(start + 1)
                # backtrack
                nums[start], nums[i] = nums[i], nums[start]
        
        n = len(nums)
        res = []
        backtrack()
        return res


nums = [1,2,3]
s=Solution()
print(s.permute(nums))
