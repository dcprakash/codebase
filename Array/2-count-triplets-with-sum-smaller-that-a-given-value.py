
def find3Numbers(A, n, X): 

	A.sort() 
	result=0
	for i in range(0,n - 2): 
			l = i + 1
			r = n - 1
			
			while (l < r): 
				if (A[i] + A[l] + A[r] >= X):
					# print("A[i]={}   A[l]={}.  A[r]={}".format(A[i],A[l],A[r]))
					r = r - 1
				else:
					print("A[i]={}   A[l]={}.  A[r]={}".format(A[i],A[l],A[r]))
					result+=(r-l)
					# print(result)
					l =l + 1
	print(result)

if __name__ == "__main__": 
	
	A = [5, 1, 3, 4, 7] 
	X = 12
	n = len(A) 
	find3Numbers(A, n, X) 

