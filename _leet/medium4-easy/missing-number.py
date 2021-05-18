'''
https://leetcode.com/problems/missing-number
    
    
'''

class Solution:
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            if i not in nums:   return i
    
    '''
    This algorithm is almost identical to the brute force approach,
    except we first insert each element of nums into a set, 
    allowing us to later query for containment in O(1) time.
    '''
    def missingNumberEff(self, nums):
        nums=set(nums)
        print(nums)
        for i in range(len(nums)+1):
            if i not in nums:   return i
        
obj=Solution()
print(obj.missingNumber([3,0,1]))
print(obj.missingNumberEff([3,0,1]))
