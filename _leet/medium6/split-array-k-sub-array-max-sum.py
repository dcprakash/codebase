# Python 3 implemenattion of the above approach 
# https://www.geeksforgeeks.org/split-the-given-array-into-k-sub-arrays-such-that-maximum-sum-of-all-sub-arrays-is-minimum/
# https://leetcode.com/problems/split-array-largest-sum/solution/

# Function to check if mid can 
# be maximum sub - arrays sum 

'''
The goal of this problem is to find the minimum largest subarray sum with m subarrays.
split array in to m subarrays, so sum of these subarrays is minimized

Instead of finding the answer directly, what if we try to guess the answer (say X), 
	and check whether this particular value could be the largest subarray sum with mm subarrays. 

Given an array of n integers and a value X, determine the minimum number of subarrays the array needs to be divided into
	such that no subarray sum is greater than X.

If the minimum number of subarrays required is less than or equal to mm then the value XX could be the largest subarray sum

instead of searching linearly for X, we can do a binary search! 
	If we can split the array into mm or fewer subarrays all with a sum that is less than or equal to X 
 	then we will try a smaller value for XX otherwise we will try a larger value for X. 
  	Each time we will select X so that we reduce the size of the search space by half.

Algorithm
1. Store the sum of elements in nums in the variable sum and the maximum element of the array in maxElement.

2. Initialize the boundary for binary search. The minimum value for the largest subarray sum is maxElement and the maximum value is equal to sum. Hence assign left and right to maxElement and sum respectively.

3. Then while the left is not greater than right:
	a. Find the mid-value in range [left, right], this is equal to the maximum subarray sum allowed. Store it in maxSumAllowed.
	b. Find the minimum number of subarrays required to have the largest subarray sum equal to maxSumAllowed.
		b.1. If the number of subarrays is less than or equal to mm then assign maxSumAllowed as the answer minimumLargestSplitSum and decrease the value of our right boundary.
		b.2. If the number of subarrays is more than mm this can't be the answer hence, increase the value of our left boundary.

4. Return minimumLargestSplitSum.

'''

class Solution:
    def splitArray(self, nums, m: int) -> int:
        
        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 0
            
            for element in nums:
                # Add element only if the sum doesn't exceed max_sum_allowed
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    # If the element addition makes sum more than max_sum_allowed
                    # Increment the splits required and reset sum
                    current_sum = element
                    splits_required += 1

            # Return the number of subarrays, which is the number of splits + 1
            return splits_required + 1
        
        # Define the left and right boundary of binary search
        left = max(nums)
        right = sum(nums)
        while left <= right:
            # Find the mid value
            max_sum_allowed = (left + right) // 2
            
            # Find the minimum splits. If splits_required is less than
            # or equal to m move towards left i.e., smaller values
            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                # Move towards right if splits_required is more than m
                left = max_sum_allowed + 1
        
        return minimum_largest_split_sum
    

nums = [7,2,5,10,8]
m = 2
s=Solution()
print(s.splitArray(nums,m))