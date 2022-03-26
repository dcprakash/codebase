'''
https://leetcode.com/problems/happy-number

It eventually gets to 11.
It eventually gets stuck in a cycle.
It keeps going higher and higher, up towards infinity.

For a number with 33 digits, it's impossible for it to ever go larger than 243243.
This means it will have to either get stuck in a cycle below 243243 or go down to 11

divmod(x, y)
x - (numerator)
y - (denominator)

returns
(q, r) - a pair of numbers (a tuple) consisting of quotient q and remainder r

dimod(8,3)
8/3; 3*2=6 so r=8-6=2; q=2

19/10; q=1, r=9
'''


class Solution:
    def isHappy(self, n):

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
    
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
    
        return n == 1

        
s=Solution()
print(s.isHappy(19))