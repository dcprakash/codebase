# https://www.geeksforgeeks.org/reverse-an-array-upto-a-given-position/

a = [1, 2, 3, 6, 8, 11]
k=3
n=len(a)
i=0
for i in range(0,int(k/2)):
    a[i],a[k-i-1]=a[k-i-1],a[i]
print(a)

'''
 0. 1. 2. 3. 4. 5. 
[1, 2, 3, 6, 8, 11]

from 0 to 1 i.e., (3/2)
a[0],a[3-0-1]=a[3-0-1],a[0]     1,3=3,1
a[1],a[3-1-1]=a[3-1-1],a[1]     2,2=2,2
'''