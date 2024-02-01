# 미로 탐험
# https://study.helloalgo.co.kr/study/1019/room/594/6486

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
    board.append(list(map(int, list(input()))))
    
q = deque()
dists = [[-1 for _ in range(M)] for _ in range(N)]

q.append((0, 0))
dists[0][0] = 1
while len(q) > 0:
    cx, cy = q.popleft()
    
    if cx == N-1 and cy == M-1:
        break
        
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and dists[nx][ny] < 0:
            q.append((nx, ny))
            dists[nx][ny] = dists[cx][cy] + 1

print(dists[N-1][M-1])
