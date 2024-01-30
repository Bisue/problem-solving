# 색종이 2(KOI지역2007_중등부_2)
# https://study.helloalgo.co.kr/study/1019/room/592/6474

import sys
sys.setrecursionlimit(10000)

dirs = [
	(-1, 0),
	(1, 0),
	(0, -1),
	(0, 1),
]

N = int(input())
H, W = 0, 0
papers = []
for _ in range(N):
	x, y = map(int, input().split())
	H, W = max(H, x+12), max(W, y+12)
	papers.append((x, y))
	
board = [[0 for _ in range(W)] for _ in range(H)]
visited = [[False for _ in range(W)] for _ in range(H)]
for x, y in papers:
	for i in range(x, x+10):
		for j in range(y, y+10):
			board[i][j] = 1

answer = 0
def dfs(x, y):
	global answer
	
	visited[x][y] = True
	
	for dx, dy in dirs:
		nx, ny = x + dx, y + dy
		if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
			answer += 1
		
	for dx, dy in dirs:
		nx, ny = x + dx, y + dy
		if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 1 and not visited[nx][ny]:
			dfs(nx, ny)
			
for x in range(H):
	for y in range(W):
		if board[x][y] == 1 and not visited[x][y]:
			dfs(x, y)
	
print(answer)
