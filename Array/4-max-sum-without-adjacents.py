# Function to return max sum such that 
# no two elements are adjacent 
# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
# https://leetcode.com/problems/house-robber/
# alternate
# adjacent
# dynamic program
# https://leetcode.com/problems/house-robber/solution/
# https://www.youtube.com/watch?v=6w60Zi1NtL8&t=3s&ab_channel=GeeksforGeeks


def find_max_sum(arr): 
	incl = 0
	excl = 0

	for i in arr: 
		excl_curr=max(incl,excl)	# max sum excluding current element i
		
		incl = excl + i		# Current max including current element i
		excl = excl_curr 
		print("for i={}, incl={}, excl={}, new_excl={}".format(i,incl,excl,excl_curr))

	# return max of incl and excl 
	return (excl if excl>incl else incl) 

# Driver program to test above function 
arr = [3, 2, 7, 10] 
print(find_max_sum(arr))


'''
Loop for all elements in arr[] and maintain two sums incl and excl where 
	incl = Max sum including the previous element  
	excl = Max sum excluding the previous element.
Max sum excluding the current element will be max(incl, excl)
max sum including the current element will be excl + current element 
(Note that only excl is considered because elements cannot be adjacent).
At the end of the loop return max of incl and excl.



'''