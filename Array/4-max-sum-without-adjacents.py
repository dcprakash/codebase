# Function to return max sum such that 
# no two elements are adjacent 
# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

def find_max_sum(arr): 
	incl = 0
	excl = 0
	
	for i in arr: 
	    new_excl=max(incl,excl)
		
		# Current max including i 
	    incl = excl + i 
	    excl = new_excl 
	    print("for i={}, incl={}, excl={}, new_excl={}".format(i,incl,excl,new_excl))
	
	# return max of incl and excl 
	return (excl if excl>incl else incl) 

# Driver program to test above function 
arr = [3, 2, 7, 10] 
print find_max_sum(arr) 
