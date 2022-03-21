"""
https://leetcode.com/problems/majority-element/solution/
"""
class Solution:
    def majorityElement(self, nums):
        mj=len(nums)//2
        for num in nums:
            count=sum(1 for element in nums if element==num)
            if count>mj:    return num
            
    def majorityElementEff(self,nums):
        from collections import Counter
        counts=Counter(nums)
        # print(counts)
        # Then, we simply return the key with maximum value.
        # we know for sure majority exist, as per question
        return max(counts.keys(), key=counts.get)
        
nums = [2,2,1,1,1,2,2]
s=Solution()
print(s.majorityElementEff(nums))
        