# 둘레
# https://study.helloalgo.co.kr/study/1019/room/592/6472

import sys
sys.setrecursionlimit(10000000)

dirs = [
	(-1, 0),
	(1, 0),
	(0, -1),
	(0, 1),
]

N = int(input())
boardSize = 105
board = [[0 for _ in range(boardSize)] for _ in range(boardSize)]
H, W = 0, 0
for _ in range(N):
	x, y = map(int, input().split())
	H = max(H, x+3)
	W = max(W, y+3)
	
	board[x][y] = 1

# outside 체크
def fillOutside(x, y):
	global board
	
	board[x][y] = 2
	for dx, dy in dirs:
		nx, ny = x + dx, y + dy
		if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
			fillOutside(nx, ny)
			
fillOutside(0, 0)

answer = 0
visited = [[False for _ in range(boardSize)] for _ in range(boardSize)]
def dfs(x, y):
	global answer
	
	if visited[x][y]: return
	
	visited[x][y] = True
	
	# 둘레(인접 outside) 카운팅
	for dx, dy in dirs:
		nx, ny = x + dx, y + dy
		if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 2:
			answer += 1
	
	# next node
	for dx, dy in dirs:
		nx, ny = x + dx, y + dy
		if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 1:
			dfs(nx, ny)
	
for x in range(H):
	for y in range(W):
		if board[x][y] == 1 and not visited[x][y]:
			dfs(x, y)
print(answer)
