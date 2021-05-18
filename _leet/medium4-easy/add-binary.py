'''

https://leetcode.com/problems/add-binary/

11
1

convert 11 and 1 to int; add those int and display in binary format


conversion
convert

8421    bit values

11->3   input 1
1 ->1   input 2

3+1=4

100->4  outupt


1111    a
0010    b
-----
1101    a^b XOR operation gives answer without carry

1111    a
0010    b
-----
0100    (a&b)<<1 AND of two inputs, shifted by one bit to left gives carry

"Normal" math is base-10 (uses symbols "0123456789"):
int("123", 10)  # == 1*(10**2) + 2*(10**1) + 3*(10**0) == 123

Binary is base-2 (uses symbols "01"):
int("101", 2)   # == 1*(2**2) + 0*(2**1) + 1*(2**0) == 5


'''


class Solution:
    def addBinary(self, a, b):
        x, y = int(a,2), int(b,2)       # 3 1
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        print(x, y)
        return bin(x)[2:]
       
        
        
obj=Solution()
print(obj.addBinary('1011','1111011'))
"""
Your module description
"""
