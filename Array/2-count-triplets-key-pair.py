
def find3Numbers(A, n, X): 

	A.sort() 
	
	for i in range(n - 2): 
			l = i + 1
			r = n - 1
			
			while (l < r): 
				if(A[i] + A[l] + A[r] == X): 
					print(A[i], ",", ",", 
						A[l], ",", A[r]) 
					l += 1
					r -= 1
				
				elif (A[i] + A[l] + A[r] < X): 
					l += 1
				elif (A[i] + A[l] + A[r]) > X:
					r -= 1


if __name__ == "__main__": 
	
	A = [1, 4, 45, 6, 10, 12] 
	X = 17
	n = len(A) 
	find3Numbers(A, n, X) 

