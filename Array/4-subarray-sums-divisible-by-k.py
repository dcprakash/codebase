# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# subarray sums divisible by k
# list comp

from collections import Counter


def subArrayDivEfficient(A,n,K):
	curr_sum=count=0
	for i in range(n):
		curr_sum=A[i]
		if curr_sum%K==0:	count+=1
		for j in range(i+1,n):
			curr_sum+=A[j]
			if curr_sum%K==0:	count+=1
	return count


def subarraysDivByK(A, K):
    P = [0]
    for x in A:
        P.append((P[-1] + x) % K)   # [0, 4, 4, 4, 2, 4, 0]

    count = Counter(P)  # Counter({4: 4, 0: 2, 2: 1})
    return sum(v*(v-1)/2 for v in count.values())


A = [4,5,0,-2,-3,1]
K = 5
print(subarraysDivByK(A,K))
print(subArrayDivEfficient(A,len(A),K))