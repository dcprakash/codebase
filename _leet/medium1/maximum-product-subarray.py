# find the contiguous subarray with max product within an array
# https://leetcode.com/problems/maximum-product-subarray/
'''
max_so_far: picked if value is steadily increasing
min_so_far: picked if current value is negative
return result
'''


class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0

        result = nums[0]

        for i in range(len(nums)):
            accu = 1
            for j in range(i, len(nums)):
                accu *= nums[j]
                result = max(result, accu)

        return result


    def maxProductEfficient(self, nums):
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            # using temp so we don't update max_so_far until min_so_far is calculated in next line
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result


nums=[2,3,-2,4]
# nums=[2,-5,3,1,-4,0,-10,2,8]
        
s=Solution()
# print(s.maxProduct(nums))
print(s.maxProductEfficient(nums))
