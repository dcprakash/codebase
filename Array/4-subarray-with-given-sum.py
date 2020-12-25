# https://www.geeksforgeeks.org/find-subarray-with-given-sum/


def subArraysum(a,n,s):
	for i in range(n):
		curr_sum=a[i]
		for j in range(i+1,n):
			if curr_sum==s:
				print("Sub array sum is b.w index {} and {}".format(i,j-1))
			elif curr_sum>s:
				break
			else:
				curr_sum+=a[j]


def subArraysumEfficient(a,n,s):
	start=0
	end=0
	curr_sum=0
	while end<n:
		curr_sum+=a[end]
		if curr_sum>s:
			start+=1
			end=start
			curr_sum=0
		elif curr_sum==s:
			print("Sub array sum is b.w index {} and {}".format(start,end))
		else:
			end+=1
	

if __name__=='__main__':
	a = [1, 4, 20, 3, 10, 5]
	n=len(a)
	s=33
	subArraysum(a,n,s)
	subArraysumEfficient(a,n,s)
