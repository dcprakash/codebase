'''
https://leetcode.com/explore/featured/card/google/62/recursion-4/484/
https://www.youtube.com/watch?v=9ciVlXZRW8s
'''

class Solution:
    def numberOfPatterns(self, m, n):
        
        def backtrack(cur_num, remain):
            if remain==0:
                return 1
            ans=0
            for next_num in range(1, 10):
                if next_num not in seen and ((cur_num, next_num) not in skip or skip[(cur_num,next_num)] in seen):
                    seen.add(next_num)
                    ans+=backtrack(next_num,remain-1)
                    seen.remove(next_num)
                return ans
        
        # (i, j): k -> to go from i to j we must pass through k
        skip = {
            (1, 3): 2,
            (3, 1): 2,
            (1, 7): 4,
            (7, 1): 4,
            (3, 9): 6,
            (9, 3): 6,
            (7, 9): 8,
            (9, 7): 8,
            (1, 9): 5,
            (9, 1): 5,
            (2, 8): 5,
            (8, 2): 5,
            (3, 7): 5,
            (7, 3): 5,
            (4, 6): 5,
            (6, 4): 5,
        }
        ans=0
        for i in range(m, n+1):
            for start in range(1, 10):
                seen=set([start])
                ans+=backtrack(start, i-1)   #started at start, we have i-1 remaining
        
        return ans
                
                
        