"""
https://leetcode.com/problems/next-permutation/
https://www.youtube.com/watch?v=9xT2Xzlo4i4&ab_channel=DEEPTITALESRA 

next permute
next permutation
"""

class Solution:
    def swap(self, nums, i1, i2):
        nums[i1],nums[i2]=nums[i2],nums[i1]
        
    def reverse(self, nums, beg, end):
        while beg<end:
            self.swap(nums,beg,end)
            beg+=1
            end-=1
    
    def nextPermute(self, nums):
        if len(nums)==1:    return
        if len(nums)==2:    return self.swap(nums,0,1)
        
        dec=len(nums)-2
        while dec>=0 and nums[dec]>=nums[dec+1]:
            dec-=1
        self.reverse(nums,dec+1,len(nums)-1)
        
        # entire input is finished, it was in accending order; its alredy in smallest possible
        if dec == -1:   return
    
        # if we are in middle of list, we have to swap with neighbor for next greater number
        next=dec+1
        while next<len(nums) and nums[next]<=nums[dec]:
            next+=1
        self.swap(nums,next,dec)
    

nums = [1,2,3]
s=Solution()
s.nextPermute(nums)
print(nums)
        
            
