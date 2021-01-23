'''
 https://leetcode.com/problems/combination-sum/submissions/
 if the remain==0; we met target, add current comb to list
 if the remain < 0; we exceed target, cease exploration
 combination sum equal to target backtracking
 possible combination of sum
 
'''


class Solution:
    def combinationSum(self, candidates, target):

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return
			
			# without start, you'll go back and get duplicate values
			# [[3, 5], [5,3], [4, 4]] instead of [[3, 5], [4, 4]]
            for i in range(start, len(candidates)): 
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results


candidates = [3,4,5]
target = 8
s=Solution()
print(s.combinationSum(candidates, target))