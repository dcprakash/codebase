# https://leetcode.com/problems/max-area-of-island/solution/
# Use DFS to count max area of an island
# find-islands.py finds number of island, this solution finds max area of found islands


class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))
        
        # call area for each element in grid
        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))


grid=[[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]
s=Solution()
print(s.maxAreaOfIsland(grid))
