# 소 그람
# https://study.helloalgo.co.kr/study/1019/room/592/6473

import sys
sys.setrecursionlimit(10001)

dirs = [
	(-1, 0),
	(1, 0),
	(0, -1),
	(0, 1),
]

N = int(input())
board = []
for i in range(N):
	board.append(list(input()))

visited = [[False for _ in range(N)] for _ in range(N)]
	
def dfs(x, y, c):
	global visited

	visited[x][y] = True
	
	for dx, dy in dirs:
		nx, ny = x + dx, y + dy
		
		if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == c and not visited[nx][ny]:
			dfs(nx, ny, c)

human = 0
for x in range(N):
	for y in range(N):
		if not visited[x][y]:
			dfs(x, y, board[x][y])
			human += 1

for x in range(N):
	for y in range(N):
		visited[x][y] = False
		if board[x][y] == 'G':
			board[x][y] = 'R'

cow = 0
for x in range(N):
	for y in range(N):
		if not visited[x][y]:
			dfs(x, y, board[x][y])
			cow += 1

print(f'{human} {cow}')
