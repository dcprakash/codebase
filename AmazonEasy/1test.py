# Python program to replace all 0 with 5 in given integer 

# A recursive function to replace all 0s with 5s in an integer 
# Does'nt work if the given number is 0 itself 
def convert0to5rec(num): 

	# Base case for recurssion termination 
	if num == 0: 
		return 0

	# Extract the last digit and change it if needed 
	digit = num % 10

	if digit == 0: 
		digit = 5

	# Convert remaining digits and append the last digit 
	return convert0to5rec(num/10) * 10 + digit 

# It handles 0 to 5 calls convert0to5rec() for other numbers 
def convert0to5(num): 
	if num == 0: 
		return 5
	else: 
		return convert0to5rec(num) 


# Driver Program 
num = 103
print convert0to5(num) 

# Contributed by Harshit Agrawal 
