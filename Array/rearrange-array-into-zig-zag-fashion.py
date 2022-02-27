# https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/
# if True then first element < second element
# if False then first element > second element

a=[4, 3, 7, 8, 6, 2, 1]
n=len(a)
flag=True
for i in range(n-1):
	if flag is True:
		if a[i]>a[i+1]:
			a[i],a[i+1]=a[i+1],a[i]
	else:
		if a[i]<a[i+1]:
			a[i],a[i+1]=a[i+1],a[i]
	flag=bool(1-flag) #flip true to false and vice versa
print(a)