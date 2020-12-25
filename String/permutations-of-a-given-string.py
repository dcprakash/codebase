# Python program to print all permutations with 
# duplicates allowed 

def toString(List): 
	return ''.join(List) 

# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 
def permute(a, l, r):
    global res
    if l==r:
        res.append(toString(a))
    else:
        for i in range(l,r+1):
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack 

# Driver program to test the above function 
res=[]
string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 
print(res)

# This code is contributed by Bhavya Jain 
