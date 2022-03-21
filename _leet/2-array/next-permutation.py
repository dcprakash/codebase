"""
https://leetcode.com/problems/next-permutation/
https://www.youtube.com/watch?v=9xT2Xzlo4i4&ab_channel=DEEPTITALESRA 

next permute
next permutation

[5,4,3,2,1]
we cannot find next greater number, so just reverse it


[1,7,9,9,8,3]
[1,7,3,8,9,9]   -> from right to left, find first smallest number and reverse upto that number
[1,8,3,7,9,9]   -> from where we left off, if list is not exausted; then find next greater number and swap with it


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
        
        dec=len(nums)-2 #start from last but one, because we cannot swap last digit with anything
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
        
            
