
def findPyTriplet(A, n, X): 

	A.sort() 
	l=0
	r=n-1
			
	while (l < r): 
		if(A[l] + A[r] == X): 
			print(A[l], ",", A[r]) 
			l += 1
			r -= 1
		
		elif (A[l] + A[r] < X): 
			l += 1
		elif (A[l] + A[r]) > X:
			r -= 1


if __name__ == "__main__": 
	
	A = [1, 4, 45, 6, 10, 12] 
	X = 16
	n = len(A) 
	findPyTriplet(A, n, X) 

