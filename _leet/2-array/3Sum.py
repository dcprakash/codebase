# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums):
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    if [nums[i],nums[l],nums[r]] not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return res
                    