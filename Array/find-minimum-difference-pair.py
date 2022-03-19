# https://www.geeksforgeeks.org/find-minimum-difference-pair/

a = [1, 19, -4, 31, 38, 25, 100] 
a.sort()    # without sort, we would have to use 2 for loops O(n)2
n = len(a) 
res=[]
mi=float('inf')
for i in range(n-1):    # because the list is now sorted, just one loop is enough
    if a[i+1]-a[i]<mi:
        mi=a[i+1]-a[i]
print(mi)
