# 알파벳
# https://www.acmicpc.net/problem/1987

# [TODO] DFS 내 가지치기 좀 더 가능할 듯.

import sys

dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

R, C = map(int, sys.stdin.readline().split())
board = []
alphas = set()
for _ in range(R):
    line = sys.stdin.readline().rstrip()
    alphas = alphas.union(set(line))
    board.append(line)   

answer = 0

visited = [False for _ in range(27)]
def dfs(cx, cy, cd):
    global answer
    
    if answer == len(alphas):
        return
    
    answer = max(answer, cd)
    
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if 0<=nx<R and 0<=ny<C:
            idx = ord(board[nx][ny]) - 65
            if not visited[idx]:
                visited[idx] = True
                dfs(nx, ny, cd + 1)
                visited[idx] = False
            
visited[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)

print(answer)
