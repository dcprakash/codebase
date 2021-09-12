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

        new = nums[:]
        for i in range(len(nums)):
            temp = nums[i]
            new[i] = new[i-1] if i > 0 else float('-inf')
            if monotone_increasing(new):
                return True
            new[i] = temp

        return False


# nums = [3,4,2,3]
nums = [4,2,3]
s=Solution()
print(s.checkPossibility(nums))
