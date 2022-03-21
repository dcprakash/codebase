'''
https://leetcode.com/problems/non-decreasing-array/
'''

class Solution:
    def checkPossibility(self, nums):
        def monotone_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = nums[i-1] if i > 0 else float('-inf')
            if monotone_increasing(nums):
                return True
            nums[i] = temp

        return False


# nums = [3,4,2,3]
nums = [4,2,3]
s=Solution()
print(s.checkPossibility(nums))
