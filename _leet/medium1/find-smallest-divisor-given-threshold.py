# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/solution/
# list comp

from math import ceil


class Solution:
    def smallestDivisor(self, nums, threshold):
        # declare lambda function; we call this for d=1 to threshold
        compute_sum = lambda x : sum([ceil(n / x) for n in nums])
        d = 1
        while compute_sum(d) > threshold:
            d += 1
        
        return d


nums = [1,2,5,9]
threshold = 6
s=Solution()
print(s.smallestDivisor(nums, threshold))
