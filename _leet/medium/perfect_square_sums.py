# https://leetcode.com/problems/perfect-squares/solution/
'''
square numbers and a positive integer number n, one is asked to find a 
    combination of square numbers that sum up to n
'''

import math


def numSquares(n):
    square_nums=[i**2 for i in range(1, int(math.sqrt(n))+1)]
    #sqrt of 12 is 3; so square_nums=[1, 4, 9]
    
    def minNumSquare(k):
        if k in square_nums:    return 1
        min_num=float('inf')
        
        for s in square_nums:
            if k<s:
                break
            new_num=minNumSquare(k-s) + 1
            min_num = min(min_num, new_num)
        return min_num
    
    return minNumSquare(n)


# Dynamic Programming
def numSquaresEfficient(n):
    square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
    #[0,1,4] for 5
    dp = [float('inf')] * (n+1)
    # bottom case
    dp[0] = 0
    
    for i in range(1, n+1):
        for square in square_nums:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i-square] + 1)
    
    return dp[-1]
    
            
n=5
# print(numSquares(n))
print(numSquaresEfficient(n))