# 토마토(KOI지역2013_초등부_3)
# https://study.helloalgo.co.kr/study/1019/room/594/6490/source/826248/

from collections import deque

dirs = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    
dists = [[-1 for _ in range(M)] for _ in range(N)]

q = deque()
for x in range(N):
    for y in range(M):
        if board[x][y] == 1:
            q.append((x, y))
            dists[x][y] = 0

while len(q) > 0:
    cx, cy = q.popleft()
    
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if 0<=nx<N and 0<=ny<M and board[nx][ny]==0 and dists[nx][ny] < 0:
            q.append((nx, ny))
            dists[nx][ny] = dists[cx][cy] + 1


maxDist, impossible = 0, False
for x in range(N):
    for y in range(M):
        maxDist = max(maxDist, dists[x][y])
        if board[x][y] == 0 and dists[x][y] < 0:
            impossible = True

if impossible:
    print(-1)
else:
    print(maxDist)
