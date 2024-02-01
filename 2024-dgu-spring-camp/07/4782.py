# 나이트의 이동
# https://study.helloalgo.co.kr/study/1019/room/594/6488/source/826190/

from collections import deque

dirs = [
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
    (-1, -2),
    (1, -2),
    (-1, 2),
    (1, 2),
]

T = int(input())
for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    
    q = deque()
    dists = [[-1 for _ in range(N)] for _ in range(N)]
    
    q.append((sx, sy))
    dists[sx][sy] = 0
    while len(q) > 0:
        cx, cy = q.popleft()
        
        if cx == ex and cy == ey:
            break
            
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and dists[nx][ny] < 0:
                q.append((nx, ny))
                dists[nx][ny] = dists[cx][cy] + 1
            
    print(dists[ex][ey])
