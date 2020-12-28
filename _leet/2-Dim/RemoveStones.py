# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solution/


from collections import defaultdict


class Solution(object):
    def removeStones(self, stones):
        graph = defaultdict(list)
        for i, x in enumerate(stones):
            for j in xrange(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in xrange(N):
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
