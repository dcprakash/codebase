"""
https://leetcode.com/problems/shortest-bridge/
https://www.youtube.com/watch?v=uH9g7aLOgiI&ab_channel=HappyCoding

use DFS to iterate all elements with 1
    if an element is 1, then find its connected graph and iterate over it
    we will have islands in seen

add seen islands to another queue
    expand the first island and do dfs again
        this time we dont need to check if its 1 but instead, we make sure its not seen yet
    increase distance to say, we have added 1
    if distance > 0:
        we have found number of flips

"""

from collections import defaultdict, deque


class Solution:
    def shortestBridge(self, A):
        matrix=A
        m=len(matrix)
        n=len(matrix[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        seen=set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    queue=deque([(i,j)])
                    seen.add((i,j))
                    
                    while queue:
                        cur_i, cur_j = queue.popleft()
                        for d in directions:
                            newi=cur_i+d[0]
                            newj=cur_j+d[1]
                            if 0<=newi<m and 0<=newj<n and matrix[newi][newj]==1 and (newi, newj) not in seen:
                                queue.append((newi,newj))
                                seen.add((newi,newj))
                    
                    # expand first island
                    queue=deque(seen)
                    dist=0
                    
                    while queue: #initially this queue has (0,1) with len=1, after first for loop iteration, queue len is 3 (includes 0,1 nei)
                        for _ in range(len(queue)): #initially queue len is 1 with value (0,1); so for loop iterate once, however queue grows into 3 (includes 0,1 nei) during this first iteration
                            cur_i, cur_j = queue.popleft()
                            if matrix[cur_i][cur_j]==1 and dist>0:  #if dist>0 means, we alrdeay seen 1
                                return dist-1
                            for d in directions:
                                newi=cur_i+d[0]
                                newj=cur_j+d[1]
                                if 0<=newi<m and 0<=newj<n and (newi, newj) not in seen:
                                    queue.append((newi,newj))
                                    seen.add((newi,newj))
                        dist+=1


matrix = [[0,1,0],
          [0,0,0],
          [0,0,1]]
s=Solution()
print(s.shortestBridge(matrix))


#{{(0, 1), (0, 2), (1, 1), (0, 0)}

