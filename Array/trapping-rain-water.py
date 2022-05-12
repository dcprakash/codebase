# https://www.geeksforgeeks.org/trapping-rain-water/
# https://leetcode.com/problems/trapping-rain-water-ii/

'''
a=3, 0, 2, 0, 4
l=3, 3, 3, 3, 4
r=4, 4, 4, 4, 4


'''

def maxWater(a):
	n=len(a)
	if n == 0:	return 0
 
	left=[None]*n
	left[0]=a[0]
	for i in range(1,n):
		left[i]=max(left[i-1],a[i])
	
	right=[None]*n
	right[n-1]=a[n-1]
	for i in range(n-2,-1,-1):
		right[i]=max(right[i+1],a[i])
		
	water=0
	for i in range(n-1):
		water+=(min(left[i],right[i])-a[i])
	
	return water
	

if __name__=='__main__':
	a = [3, 0, 2, 0, 4]
	# a=[0,1,0,2,1,0,1,3,2,1,2,1]
	print("Max water={}".format(maxWater(a)))
