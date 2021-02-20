# https://www.geeksforgeeks.org/reverse-an-array-upto-a-given-position/

a = [1, 2, 3, 4, 5, 6]
k=4
n=len(a)
i=0
for i in range(0,int(k/2)):
	a[i],a[k-i-1]=a[k-i-1],a[i]
print(a)