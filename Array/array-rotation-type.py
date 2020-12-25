# https://www.geeksforgeeks.org/type-array-maximum-element

def findArrayRot(a,n):
    i=0
    while (i<n-1 and a[i]<a[i+1]):
        i+=1
    if i==n-1:
        print("Ascending Array")
        
    if i==0:
        while i<n-1 and a[i]>a[i+1]:
            i+=1
        if i==n-1:
            print("Descending Array")
        
        if a[0]<a[i+1]:
            print("Descending Rotated Array")
        
        else:
            print("Ascending Rotated Array")
    
    if i<n-1 and a[0]>a[i+1]:
        print("Ascending Rotated Array")
    else:
        print("Descending Rotated Array")
            

a1=[1, 3, 5, 9]
a2=[5, 3, 2, 1]
a3=[2, 1, 5, 4]
a4=[3, 4, 1, 2]
findArrayRot(a4,len(a4))