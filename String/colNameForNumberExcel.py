# Python program to find Excel column name from a 
# given column number

MAX = 50

# Function to print Excel column name 
# for a given column number
def printString(n):

	# To store result (Excel column name)
	string = ["\0"] * MAX

	# To store current index in str which is result
	i = 0

	while n > 0:
		# Find remainder
		rem = n % 26

		# if remainder is 0, then a 
		# 'Z' must be there in output
		if rem == 0:
			string[i] = 'Z'
			i += 1
			n = (n // 26) - 1
		else:
			# convert number like 25 to its alpha equivalent by
			# ord('A') + 25-1 = 'Y'
			string[i] = chr((rem - 1) + ord('A'))
			i += 1
			n = n // 26
	string[i] = '\0'

	# Reverse the string and print result
	string = string[::-1]
	print("".join(string))

# Driver program to test the above Function
# printString(26)
printString(51)
printString(52)
