#// https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1


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
	
	A = [0, -1, 2, -3, 1] 
	X = 0
	n = len(A) 
	find3Numbers(A, n, X) 

