# 점이 두개(중간고사)
# https://study.helloalgo.co.kr/exam/616/solve/3991

from collections import deque

dirs = [
	(-1, 0),
	(1, 0),
	(0, -1),
	(0, 1),
]

N, M = map(int, input().split())
board = []
for _ in range(N):
	board.append(input())
	
islands = [[0 for _ in range(M)] for _ in range(N)]

# 점 영역을 1번 점, 2번 점으로 구분
visited = set()
curIslandId = 1
for x in range(N):
	for y in range(M):
		if board[x][y] == 'X' and (x, y) not in visited:
			q = deque()
			q.append((x, y))
			visited.add((x, y))
			while len(q) > 0:
				cx, cy = q.popleft()
				
				islands[cx][cy] = curIslandId
				
				for dx, dy in dirs:
					nx, ny = cx + dx, cy + dy
					if 0<=nx<N and 0<=ny<M and board[nx][ny] == 'X' and (nx, ny) not in visited:
						q.append((nx, ny))
						visited.add((nx, ny))
						
			curIslandId += 1

answer = 1e10

# 1번 점의 모든 시작점 큐에 삽입
q = deque()
visited = set()
for x in range(N):
	for y in range(M):
		if islands[x][y] == 1:
			q.append((x, y, 0))
			visited.add((x, y))

# target(2번 점)에 도달할 때까지 bfs
# (dist 대소비교 말고 visited True False 체크만으로 되나? - 검증 필요)
target = 2
while len(q) > 0:
	cx, cy, cd = q.popleft()

	if islands[cx][cy] == target:
		answer = min(answer, cd-1)
		break

	for dx, dy in dirs:
		nx, ny = cx + dx, cy + dy
		if 0<=nx<N and 0<=ny<M and board[nx][ny] != islands[x][y] and (nx, ny) not in visited:
			q.append((nx, ny, cd + 1))
			visited.add((nx, ny))
						
print(answer)
