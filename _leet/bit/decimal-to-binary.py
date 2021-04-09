"""
https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/

"""

def decimalToBinaryBuiltin(num):
    return bin(num)[2:]
    
def decimalToBinary(num):
    return (decimalToBinary(num//2) + str(num%2)) if num>=1 else ''

print(decimalToBinaryBuiltin(5))
print(decimalToBinary(5))
