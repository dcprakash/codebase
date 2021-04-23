"""
https://leetcode.com/problems/powx-n/

multiply x for n times

If n<0, we can substitute x with 1/x
        and make -n to n
"""


def power(x,n):
    Neg=n
    if Neg<0:
        x=1/x
        Neg=-Neg
    ans=1
    
    for _ in range(Neg):
        ans=ans*x
    return ans


# x = 2
# n = 3

x = 2.00000
n = -2

print(power(x,n))

        
    
