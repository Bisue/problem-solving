# 침투
# https://study.helloalgo.co.kr/study/1019/room/592/6471

import sys

sys.setrecursionlimit(1000000)

dirs = [
	(-1, 0),
	(1, 0),
	(0, -1),
	(0, 1)
]

N, M = map(int, input().split())
board = []
for _ in range(N):
	board.append(list(map(int, list(input()))))

found = False
def dfs(x, y):
	global found, board
	
	board[x][y] = 2 # fill visited
	if x == N-1:
		found = True
	
	if found:
		return
	
	for dx, dy in dirs:
		nx, ny = x + dx, y + dy
		if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
			dfs(nx, ny)

for y in range(M):
	if board[0][y] == 0 and not found:
		dfs(0, y)
		
answer = 'YES' if found else 'NO'
print(answer)
