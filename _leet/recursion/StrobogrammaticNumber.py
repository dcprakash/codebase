'''
https://leetcode.com/explore/interview/card/facebook/53/recursion-3/3029/

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
inverse number
'''

# Python program to print all 
# Strobogrammatic number of length n 
'''
n=1
	["1", "0", "8"]
n=2
	middle=""
	8+middle+8=88
	['88', '11', '96', '69']
n=3
	middle=[1,0,8]
	for item in middle:
		8+item+8=818
	['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']
n=4
	middle=['00', '88', '11', '96', '69']
	for item in middle:
		8+item=8=8008,8888,8118,, etc
	['8008', '1001', '9006', '6009', '8888', '1881', '9886', '6889', '8118', 
	'1111', '9116', '6119', '8968', '1961', '9966', '6969', '8698', '1691', '9696', '6699']
	


'''

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
	print(strobogrammatic_num(3)) 
