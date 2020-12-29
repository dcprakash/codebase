# Python 3 implemenattion of the above approach 
# https://www.geeksforgeeks.org/split-the-given-array-into-k-sub-arrays-such-that-maximum-sum-of-all-sub-arrays-is-minimum/
# https://leetcode.com/problems/split-array-largest-sum/solution/

# Function to check if mid can 
# be maximum sub - arrays sum 
def check(mid, array, n, K): 
	count = 0
	sum = 0
	for i in range(n): 
		
		# If individual element is greater 
		# maximum possible sum 
		if (array[i] > mid): 
			return False

		# Increase sum of current sub - array 
		sum += array[i] 

		# If the sum is greater than 
		# mid increase count 
		if (sum > mid): 
			count += 1
			sum = array[i] #update sum to current element to adding can go on
	count += 1

	# Check condition 
	if (count <= K): 
		return True
	return False

# Function to find maximum subarray sum 
# which is minimum 
def solve(array, n, K): 
	start = 1
	end = 0

	for i in range(n): 
		end += array[i] 

	# Answer stores possible 
	# maximum sub array sum 
	answer = 0
	while (start <= end): 
		mid = (start + end) // 2

		# If mid is possible solution 
		# Put answer = mid; 
		if (check(mid, array, n, K)): 
			answer = mid 
			end = mid - 1
		else: 
			start = mid + 1

	return answer 

# Driver Code 
if __name__ == '__main__': 
	array = [1, 2, 3, 4] 
	n = len(array) 
	K = 2
	print(solve(array, n, K))

# continuos sub array i.e., 1+2+3=6, 4
# otherwise, 1+2=3, 4+3=7
# 6 is better choice