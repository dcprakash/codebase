"""
https://leetcode.com/problems/shortest-bridge/
https://www.youtube.com/watch?v=uH9g7aLOgiI&ab_channel=HappyCoding

"""
from collections import defaultdict, deque


class Solution:
    def shortestBridge(self, matrix):
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
                    
                    while queue:
                        for _ in range(len(queue)):
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


matrix = [[0,1,0],[0,0,0],[0,0,1]]
s=Solution()
print(s.shortestBridge(matrix))