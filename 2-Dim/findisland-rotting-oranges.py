# https://leetcode.com/problems/rotting-oranges/solution/
# find islands max area, BFS, fresh oranges, rotten oranges
'''
[
[2,1,1],
[1,1,0],
[0,1,1]
]


'''

from collections import deque


class Solution:
    
    def orangesRotting(self, grid):
        rotten_queue = deque()
        fresh_oranges = 0

        # Step 1). build the initial set of rotten oranges queue
        # and fresh oranges count
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        rotten_queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while rotten_queue:
            row, col = rotten_queue.popleft()
            if row == -1:
                # We finish one round of processing
                # We use a delimiter (i.e. (row=-1, col=-1)) in the queue to separate cells on different levels.
                minutes_elapsed += 1
                if rotten_queue:  # to avoid the endless loop
                    rotten_queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            rotten_queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1


s=Solution()
# grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(s.orangesRotting(grid))