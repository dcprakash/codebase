# https://www.geeksforgeeks.org/array-rotation/

def leftrotatearray(a,n,r):
    while r:
        for i in range(n-1):
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
        r-=1
    print(a)


a = [1, 3, 4, 6]
n=len(a)
r=2
print(a)
leftrotatearray(a,n,r)
