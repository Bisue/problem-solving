# 미로 제작
# https://study.helloalgo.co.kr/study/1019/room/600/6572

# 검은 방 바꾼 횟수(통과한 횟수)가 가장 적은 것부터 방문
# attempts[x][y] == x, y까지 가는데 필요한 바꿈 횟수

import sys
import heapq as hq

dirs = [
	(-1, 0),
	(1, 0),
	(0, -1),
	(0, 1),
]

N = int(sys.stdin.readline().rstrip())
board = []
for _ in range(N):
	board.append(sys.stdin.readline().rstrip())
	
pq = []
attemps = [[1e10 for _ in range(N)] for _ in range(N)]

hq.heappush(pq, (0, 0, 0))
attemps[0][0] = 0

while len(pq) > 0:
	ca, cx, cy = hq.heappop(pq)
	if ca > attemps[cx][cy]:
		continue
	
	if cx == N-1 and cy == N-1:
		break
	
	for dx, dy in dirs:
		nx, ny = cx+dx, cy+dy
		
		if 0<=nx<N and 0<=ny<N:
			na = ca
			if board[nx][ny]=='0':
				na += 1
				
			if na < attemps[nx][ny]:
				hq.heappush(pq, (na, nx, ny))
				attemps[nx][ny] = na
		
print(attemps[N-1][N-1])
