# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
# https://leetcode.com/problems/coin-change/solution/
# https://www.youtube.com/watch?v=jgiZlGzXMBw&feature=emb_logo&ab_channel=BackToBackSWE

# A Naive recursive python program to find minimum of coins 
# to make a given change V 

import sys 

# m is size of coins array (number of different coins) 
def minCoins(coins, n, amount): 
	
	# base case 
	if (amount == 0): 
		return 0

	# Initialize result 
	res = sys.maxsize 
	
	# Try every coin that has smaller value than amount
	for i in range(0, n): 
		if (coins[i] <= amount): 
			sub_res = minCoins(coins, n, amount-coins[i]) 

			# Check for INT_MAX to avoid overflow and see if 
			# result can minimized 
			if (sub_res != sys.maxsize and sub_res + 1 < res): 
				res = sub_res + 1

	return res 

# Driver program to test above function 
coins = [1,2,5] 
n = len(coins) 
amount = 3
print("Minimum coins required is",minCoins(coins, n, amount)) 
