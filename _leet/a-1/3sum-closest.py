'''
https://leetcode.com/problems/3sum-closest/

Initialize the minimum difference diff with a large value.
Sort the input array nums.
Iterate through the array:
    For the current position i, set lo to i + 1, and hi to the last index.
    While the lo pointer is smaller than hi:
        Set sum to nums[i] + nums[lo] + nums[hi].
        If the absolute difference between sum and target is smaller than the absolute value of diff:
            Set diff to target - sum.
        If sum is less than target, increment lo.
        Else, decrement hi.
    If diff is zero, break from the loop.
Return the value of the closest triplet, which is target - diff.    

to get 3 sum closest as possible to target, 
    we can iteratively in 3 for loops add all possbilities of 3 numbers
    if sum of 3 numbers - taget < diff (we already have, initially max value)
        we replace the diff
'''

class Solution:
    def threeSumClosest(self, nums, target):
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:   # mean we found 3 numbers exactly equal to target
                break
        return target - diff
        

sol=Solution()
print(sol.threeSumClosest([-1,2,1,-4],1))