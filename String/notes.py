from math import ceil


class Solution:
    def smallestDivisor(self, nums, threshold):
        compute = lambda x: sum([ceil(n/x) for n in nums])
        d=1
        while compute(d)>threshold:
        	d+=1
        return d


nums = [1,2,5,9]
threshold = 6
s=Solution()
print(s.smallestDivisor(nums, threshold))