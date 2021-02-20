# https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/

# easy method, may not be what question is asking as this changes order
# a=[-1, 2, -3, 4, 5, 6, -7, 8, 9]
a=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
a.sort()
n=len(a)
l=0
r=n-1
rflag=True
res=[]
while l<=r:
	if rflag:
		res.append(a[r])
		r-=1
	else:
		res.append(a[l])
		l+=1
	rflag=bool(1-rflag)
print(res)
	
	
	