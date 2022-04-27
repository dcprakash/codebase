'''
https://leetcode.com/problems/combination-sum-ii/
we are not allowed to use same number again, so we keep counter of input array. Each time we use a candidate, we -1 the counter

combination sum
'''


import collections


class Solution:
    def combinationSum2(self, candidates, target):

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return
			
            for i in range(start, len(counter)):
                candidate, freq = counter[i]
                if freq <= 0:
                    continue
                
                # add the number into the combination
                comb.append(candidate)
                counter[i] = (candidate, freq-1)
                
                # give the current number another chance, rather than moving on
                backtrack(remain - candidate, comb, i)
                
                # backtrack, remove the number from the combination
                counter[i] = (candidate, freq)
                comb.pop()


        results = []
        counter = collections.Counter(candidates)   #Counter({1: 2, 10: 1, 2: 1, 7: 1, 6: 1, 5: 1})
        # convert the counter table to a list of (num, count) tuples
        counter = [(c, counter[c]) for c in counter]    #[(10, 1), (1, 2), (2, 1), (7, 1), (6, 1), (5, 1)]
        backtrack(target, [], 0)

        return results

candidates = [10,1,2,7,6,1,5]
target = 8
s=Solution()
print(s.combinationSum2(candidates, target))