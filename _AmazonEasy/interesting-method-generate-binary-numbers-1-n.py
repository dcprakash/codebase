# https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/

def convertToBinary(n):
    global s
    if n > 1:
       convertToBinary(n//2)
    s+=str(n % 2)


print(9//2) # // give reminder
s=''
convertToBinary(3)
print s
# if __name__=='__main__':
#     dec = 5
#     s = ''
#     for i in range(dec):
#         convertToBinary(i)
#         print("Binary rep for {} is {}".format(i, s))
#         s = ''
