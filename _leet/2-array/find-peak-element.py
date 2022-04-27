# https://leetcode.com/problems/find-peak-element/
# peak element in an array or list
# Whenever, we find a number nums[i]nums[i], we only need to check if it is larger than
# the next number nums[i+1]nums[i+1] for determining if nums[i]nums[i] is the peak element
# no need to check nums[i-1]<nums[i]
# if nums[i-1]<nums[i]>nums[i+1]: 


class Solution:
    def findPeakElement(self, nums):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return i
        return len(nums)-1  # corner case if list has 1 element
        
        
    def search(self, nums, l, r):
        if l==r:    return l
        mid = (l+r)//2;
        if nums[mid]>nums[mid+1]:   return self.search(nums, l, mid) #mid=1 i.e., 3 which is greater than 2, since we found 1st of condition to prove preak elemend, now we check if element behind mid is smaller by searching on left of the array
        else:   return self.search(nums, mid+1, r)
        
        
    def findPeakElementBinarySearch(self, nums):
        return self.search(nums, 0, len(nums)-1)
        
    #.  0 1 2 3
nums = [1,3,2,1]
s=Solution()
#print(s.findPeakElement(nums))
print(s.findPeakElementBinarySearch(nums))

'''
We start off by finding the middle element, midmid from the given numsnums array. 
    If this element happens to be lying in a descending sequence of numbers
    it means that the peak will always lie towards the left of this element. 
    Thus, we reduce the search space to the left
    
If the middle element, midmid lies in an ascending sequence of numbers, or a rising slope
    it obviously implies that the peak lies towards the right of this element.

In this way, we keep on reducing the search space till we eventually reach a state 
    where only one element is remaining in the search space. 
    This single element is the peak element
'''