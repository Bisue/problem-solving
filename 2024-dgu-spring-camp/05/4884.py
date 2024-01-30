# 섬의 개수
# https://study.helloalgo.co.kr/study/1019/room/592/6470

dirs = [
	(-1, -1),
	(-1, 0),
	(-1, 1),
	(0, -1),
	(0, 1),
	(1, -1),
	(1, 0),
	(1, 1)
]

while True:
	w, h = map(int, input().split())
	if w == 0 and h == 0:
		break
	
	board = []
	for _ in range(h):
		board.append(list(map(int, input().split())))
		
	visited = set()
	
	def fillDfs(x, y):
		visited.add((x, y))
		
		for dx, dy in dirs:
			nx, ny = x + dx, y + dy
			if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1 and (nx, ny) not in visited:
				fillDfs(nx, ny)
				
	answer = 0
	for x in range(h):
		for y in range(w):
			if board[x][y] == 1 and (x, y) not in visited:
				fillDfs(x, y)
				answer += 1
				
	print(answer)
				


