# https://www.geeksforgeeks.org/reverse-an-array-in-groups-of-given-size/

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k=3
n=len(a)
i=0
while i<n:
	l=i
	r=min(i+k-1, n-1)
	while l<r:
		a[l],a[r]=a[r],a[l]
		l+=1
		r-=1
	i+=k
print(a)
