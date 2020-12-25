"""
https://leetcode.com/problems/divide-two-integers/solution/
"""
dividend = 7
divisor = -3

negatives=0

if dividend < 0:
    negatives+=1
    dividend=-dividend
    
if divisor < 0:
    negatives+=1
    divisor=-divisor


subtractions=0

while dividend-divisor >= 0:
    dividend-=divisor
    subtractions+=1
    
if negatives==1:
    subtractions=-subtractions
    
print(subtractions)
    
    