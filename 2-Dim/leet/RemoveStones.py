# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solution/


from collections import defaultdict


class Solution(object):
    def removeStones(self, stones):
        graph = defaultdict(list)
        for i, x in enumerate(stones):
            for j, y in enumerate(stones[:i]):
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        print(graph)
        # {0: [1, 3], 1: [0, 4], 3: [0, 4], 4: [1, 3]}
        N = len(stones)
        ans = 0
        seen = [False] * N
        
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans


s=Solution()
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print(s.removeStones(stones))

'''
   0     1     2     3     4
[[0,0],[0,2],[1,1],[2,0],[2,2]]
{0: [1, 3], 1: [0, 4], 3: [0, 4], 4: [1, 3]}
for 0th stone, we have 1st and 3rd stone in same column and row

compare 0,0 and 0,2
if 0==0 or 0==2:
    create defaultdict

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
  
   0 1 2
0  1 0 1
1  0 1 0
2  1 0 1

create defaultdict list of all nodes that has stones
seen = [False, False, False, False, False] 
seen is used to mark where stone is removed
use DFS to remove stones

Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

'''