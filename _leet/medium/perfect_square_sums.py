# https://leetcode.com/problems/perfect-squares/solution/
'''
square numbers and a positive integer number n, one is asked to find a 
    combination of square numbers that sum up to n
'''

import math


def numSquares(n):
    square_nums=[i**2 for i in range(1, int(math.sqrt(n))+1)]
    #sqrt of 12 is 3; so square_nums=[1, 4, 9]
    
    def minNumSquare(n):
        # subtrack n-s until we return 1
        if n in square_nums:    return 1
        min_num=float('inf')
        
        for s in square_nums:
            if n<s:
                break
            new_num=minNumSquare(n-s) + 1
            min_num = min(min_num, new_num)
        return min_num
    
    return minNumSquare(n)


# Dynamic Programming
def numSquaresEfficient(n):
    square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
    #[0,1,4] for 5                0.   1.    2.   3.   4.   5.   
    dp = [float('inf')] * (n+1) #[inf, inf, inf, inf, inf, inf]
    # bottom case
    dp[0] = 0                   #[0,   inf, inf, inf, inf, inf]
    
    for i in range(1, n+1):
        for square in square_nums:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i-square] + 1)
    # [0, 1, 2, 3, 1, 2]
    return dp[-1]
    
            
n=5
print(numSquares(n))
# print(numSquaresEfficient(n))