# 벽 부수고 이동하기
# https://study.helloalgo.co.kr/study/1019/room/594/6492/source/826244/

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
q.append((0, 0, 1)) # x, y, 남은 부술 수 있는 횟수
dists = [[[1e10, 1e10] for _ in range(M)] for _ in range(N)] # dists[x][y][남은 부술 수 있는 횟수]
dists[0][0][1] = 1

escape = False
while len(q) > 0:
    cx, cy, cp = q.popleft()
    
    if cx == N-1 and cy == M-1:
        escape = True
        break # break ?
        
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < N and 0 <= ny < M:
            # 부술 수 있는 횟수가 남아있고, nx, ny가 벽이고, 이전에 간 거리보다 작게 갈 수 있다면
            if cp > 0 and board[nx][ny] == 1 and dists[cx][cy][cp] + 1 < dists[nx][ny][cp-1]:
                q.append((nx, ny, cp - 1))
                dists[nx][ny][cp-1] = dists[cx][cy][cp] + 1
            # 빈 공간이고, 이전에 간 거리보다 작게 갈 수 있다면
            elif board[nx][ny] == 0 and dists[cx][cy][cp] + 1 < dists[nx][ny][cp]:
                q.append((nx, ny, cp))
                dists[nx][ny][cp] = dists[cx][cy][cp] + 1
        
if not escape:
    print(-1)
else:
    print(min(dists[N-1][M-1]))
