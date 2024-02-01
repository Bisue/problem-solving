# 탈출하기
# https://study.helloalgo.co.kr/study/1019/room/594/6493

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
    
q = deque()
visited = set()
    
sx, sy = None, None
ex, ey = None, None
for x in range(N):
    for y in range(M):
        if board[x][y] == 'S':
            sx, sy = x, y
        elif board[x][y] == '*':
            q.append((x, y, '*', 0))
            visited.add((x, y))
        elif board[x][y] == 'D':
            ex, ey = x, y
q.append((sx, sy, 'S', 0))
visited.add((sx, sy))

possible = False
while len(q) > 0:
    cx, cy, ct, cd = q.popleft()
    
    if cx == ex and cy == ey and ct == 'S':
        print(cd)
        possible = True
        break
        
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if 0<=nx<N and 0<=ny<M and (nx, ny) not in visited:
            if ct == 'S' and board[nx][ny] in ['.', 'D']:
                q.append((nx, ny, ct, cd + 1))
                visited.add((nx, ny))
            elif ct == '*' and board[nx][ny] == '.':
                q.append((nx, ny, ct, cd + 1))
                visited.add((nx, ny))
        
if not possible:
    print('KAKTUS')
