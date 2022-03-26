# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
# https://leetcode.com/problems/coin-change/solution/
# https://www.youtube.com/watch?v=jgiZlGzXMBw&feature=emb_logo&ab_channel=BackToBackSWE

# A Naive recursive python program to find minimum of coins 
# to make a given change V 
# backtrack

import sys 

# m is size of coins array (number of different coins) 
def coinChange(coins, n, amount): 
    res = sys.maxsize
    
    def backtrack(remain, comb, start):
        nonlocal res
        if remain==0:
            res=min(res,len(comb))
        if remain<0:
            return
        for i in range(start, len(coins)):
            comb.append(coins[i])
            backtrack(remain-coins[i], comb, i)
            comb.pop()
            
    backtrack(amount, [], 0)
    return -1 if res==sys.maxsize else res
    
    
# def coinChangeEff(coins, amount):
#     dp = [0] + [float('inf')] * amount  # [0, inf, inf, inf]
    
#     for coin in coins:
#         for i in range(coin, amount+1):
#             dp[i] = min(dp[i], dp[i-coin]+1)
        
#     return dp[-1] if dp[-1] != float('inf') else -1
    
    
# def coinChangeMethod(coins, amount):  
#     # base case 
#     if (amount == 0): 
#         return 0

#     # Initialize result 
#     res = sys.maxsize 
#     n=len(coins)
#     # Try every coin that has smaller value than amount
#     for i in range(0, n): 
#         if (coins[i] <= amount): 
#             sub_res = coinChangeMethod(coins, amount-coins[i]) 

#             # Check for INT_MAX to avoid overflow and see if 
#             # result can minimized 
#             if (sub_res != sys.maxsize and sub_res + 1 < res): 
#                 res = sub_res + 1

#     return res

 
# Driver program to test above function 
coins = [3,7,405,436]
n = len(coins) 
amount = 8839
print("Minimum coins required is",coinChange(coins, n, amount))
# print("Minimum coins required is",coinChangeEff(coins, amount))
