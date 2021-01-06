"""
https://leetcode.com/problems/powx-n/
"""


def power(x,n):
    Neg=n
    if Neg<0:
        x=1/x
        Neg=-Neg
    ans=1
    
    for i in range(Neg):
        ans=ans*x
    return ans


x = 4.0
n = -2
print(power(x,n))

        
    
