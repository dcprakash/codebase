# https://www.geeksforgeeks.org/return-a-pair-with-maximum-product-in-array-of-integers/
# Input: arr[] = {1, 4, 3, 6, 7, 0}  
# Output: {6,7}  

# Input: arr[] = {-1, -3, -4, 2, 0, -5} 
# Output: {-4,-5}


def findMaxProdKeyPair(a,n):
    a.sort()
    psum=a[n-2]*a[n-1]
    nsum=a[0]*a[1]
    if psum>nsum:
        print(a[n-2],a[n-1])
    else:
        print(a[0],a[1])


#a=[1, 4, 3, 6, 7, 0]
a=[-1, -3, -4, 2, 0, -5]
n=len(a)
findMaxProdKeyPair(a,n)
