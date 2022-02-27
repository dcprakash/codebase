
# https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/

# can use dictionary

# Given a sorted array arr[] and a number x, 
# write a function that counts the occurrences of x in arr[]. 

# Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 1
#   Output: 2 


# #o(n)
# arr1 = [1, 1, 2, 2, 2, 2, 3]
# x = 2
# d={}
# for i in arr1:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d[x])

# O(nlongn)
def findOcuurence(a,n,x,left):
    l=0
    r=n-1
    result=0
    while l<=r:
        m=(l+r)//2;
        if a[m]==x:
            if left:
                r=m-1
            else:
                l=m+1
            result=m
        elif x<a[m]:
            r=m-1
        else:
            l=m+1
    return result



a=[1, 2, 2, 2, 2, 2, 2,3, 4, 8]
n=len(a)
x=2
leftIndex=findOcuurence(a,n,x,True)
rightIndex=findOcuurence(a,n,x,False)
print(leftIndex,rightIndex) #number of occurence is in rightindex

        