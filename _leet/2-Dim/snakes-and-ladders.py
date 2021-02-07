# https://leetcode.com/problems/snakes-and-ladders/solution/
# https://www.youtube.com/watch?v=1pMNYQmtVVg&ab_channel=GeeksforGeeks

'''
DFS
to go from s to s2, we need to know new corrdiantes i.e., get(s2)
row changes every N squares, quot = (s2-1) / N
column is based on rem = (s2-1) % N
'''
from collections import deque

def snakesAndLadders(board):
    N = len(board)

    def get(s):
        # Given a square num s, return board coordinates (r, c)
        quot, rem = divmod(s-1, N)  #8/6 gives 1,2 respectively
        row = N - 1 - quot
        col = rem if row%2 != N%2 else N - 1 - rem
        return row, col

    dist = {1: 0}   # {1: 0, 15: 1} ; came to 15 from 1
    queue = deque([1])
    while queue:
        s = queue.popleft()
        if s == N*N:
            print(dist)
            return dist[s]
        for s2 in range(s+1, min(s+6, N*N) + 1): #from 1 to min(7,36) positions
            r, c = get(s2)
            if board[r][c] != -1:
                s2 = board[r][c]
            if s2 not in dist:
                dist[s2] = dist[s] + 1
                queue.append(s2)
    return -1


Input = [
[-1,-1,-1,-1,-1,-1], #5
[-1,-1,-1,-1,-1,-1], #4
[-1,-1,-1,-1,-1,-1], #3
[-1,35,-1,-1,13,-1], #2
[-1,-1,-1,-1,-1,-1], #1
[-1,15,-1,-1,-1,-1]] #0
# 0. 1. 2. 3. 4. 5. 
print(snakesAndLadders(Input))