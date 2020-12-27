# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3013/

def convert(x):
    i=0
    for power, char in enumerate(x[::-1]):
        i+=pattern[char] * (10**power)
    return i
    

num1 = "200"
num2 = "3"
pattern = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
product=convert(num1) * convert(num2)
print(product)
    