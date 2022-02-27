# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# Condition, requires a negative integer
# kadane
# kadne

def maxSubArraySum(a,size): 
	
	max_so_far = 0
	max_ending_here = 0
	
	for i in range(0, size): 
		max_ending_here = max_ending_here + a[i] 
		if max_ending_here < 0: 
			max_ending_here = 0
		
		# Do not compare for all elements. Compare only 
		# when max_ending_here > 0 
		elif (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
			
	return max_so_far 
	

def maxSubArraySumGreedy(a, n):
	max_sum = cur_sum = a[0]
	for i in range(1, n):
		cur_sum=max(a[i], cur_sum+a[i])
		max_sum=max(cur_sum, max_sum)
	return max_sum
	
	
# a=[-2,1,-3,4,-1,2,1,-5,4]
# a=[-2147483647]
a=[-1]
n=len(a)
# print(maxSubArraySum(a,n))
print(maxSubArraySumGreedy(a,n))


	
