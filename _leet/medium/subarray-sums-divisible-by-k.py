# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# subarray sums divisible by k

from collections import Counter


def subarraysDivByK(A, K):
    P = [0]
    for x in A:
        P.append((P[-1] + x) % K)   # [0, 4, 4, 4, 2, 4, 0]

    count = Counter(P)  # Counter({4: 4, 0: 2, 2: 1})
    return sum(v*(v-1)/2 for v in count.values())


A = [4,5,0,-2,-3,1]
K = 5
print(subarraysDivByK(A,K))