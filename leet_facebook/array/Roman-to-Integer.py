"""
https://leetcode.com/problems/roman-to-integer/

SYMBOL       VALUE
  I            1
  IV           4
  V            5
  IX           9
  X            10
  XL           40
  L            50
  XC           90
  C            100
  CD           400
  D            500
  CM           900 
  M            1000  
  
* If I comes before V or X, subtract 1 eg: IV = 4 and IX = 9
* If X comes before L or C, subtract 10 eg: XL = 40 and XC = 90
* If C comes before D or M, subtract 100 eg: CD = 400 and CM = 900
"""


# Python program to convert Roman Numerals
# to Numbers

# This function returns value of each Roman symbol


def romanToDecimal(s):
    total = 0
    i = 0
    while i < len(s):
        # If this is the subtractive case.
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total += values[s[i + 1]] - values[s[i]]
            i += 2
        # Else this is NOT the subtractive case.
        else:
            total += values[s[i]]
            i += 1
    return total


# Driver code
print("Integer form of Roman Numeral is"),
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
print(romanToDecimal("IV"))
