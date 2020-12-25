# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1


def sort012(a,n):
	zeroc=0
	onec=0
	twoc=0
	res=[]
	for i in range(n):
		if a[i]==0:
			zeroc+=1
		elif a[i]==1:
			onec+=1
		elif a[i]==2:
			twoc+=1
	while zeroc:
		res.append(0)
		zeroc-=1
	while onec:
		res.append(1)
		onec-=1
	while twoc:
		res.append(2)
		twoc-=1
	print(res)
		


if __name__=='__main__':
	a = [0, 2, 1, 2, 0]
	n=len(a)
	sort012(a,n)
	
	a.sort()
	print(a)
	
	a.sort(reverse=True)
	print(a)
