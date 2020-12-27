'''
https://leetcode.com/explore/interview/card/facebook/53/recursion-3/3029/
'''

# Python program to print all 
# Strobogrammatic number of length n 

# strobogrammatic function 
def strobogrammatic_num(n): 
	
	result = numdef(n, n) 
	return result 
	
# definition function 
def numdef(n, length): 
	
	if n == 0: return [""] 
	if n == 1: return ["1", "0", "8"] 
	
	middles = numdef(n - 2, length) 
	result = [] 
	
	for middle in middles: 
		if n != length:			 
			result.append("0" + middle + "0") 

		result.append("8" + middle + "8") 
		result.append("1" + middle + "1") 
		result.append("9" + middle + "6") 
		result.append("6" + middle + "9") 
	return result 

# Driver Code 
if __name__ == '__main__': 
	
	# Print all Strobogrammatic 
	# number for n = 3 
	print(strobogrammatic_num(4)) 
