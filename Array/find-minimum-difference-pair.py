# https://www.geeksforgeeks.org/find-minimum-difference-pair/

a = [1, 19, -4, 31, 38, 25, 100] 
a.sort()
n = len(a) 
res=[]
mi=float('inf')
for i in range(n-1):
    if a[i+1]-a[i]<mi:
        mi=a[i+1]-a[i]
print(mi)
