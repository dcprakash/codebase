"""
https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
5>=1            1   5%2
    2>=1        0   2%2
        1>=1    1   1%2

"""

def decimalToBinaryBuiltin(num):
    return bin(num)[2:] # remove first 2 char 0b101
    
    
def decimalToBinary(num):
    return (decimalToBinary(num//2) + str(num%2)) if num>=1 else ''
    
    
def DecimalToBinaryExplained(num):
    if num >= 1:
        DecimalToBinaryExplained(num // 2)
    print(num % 2, end = '')


print(decimalToBinaryBuiltin(5))
print(decimalToBinary(5))

