# 방 개수 세기
# https://study.helloalgo.co.kr/study/1019/room/592/6468/source/825850/

from collections import deque

dirs = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

visited = set()
q = deque()

def isValid(x, y):
    return 0 <= x < n and 0 <= y < m
    
cntRooms = 0
for x in range(n):
    for y in range(m):
        if board[x][y] == '.' and (x, y) not in visited:
            cntRooms += 1
            visited.add((x, y))
            q.append((x, y))
            
            while len(q) > 0:
                cx, cy = q.popleft()
                
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if isValid(nx, ny) and board[nx][ny] == '.' and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
                        
print(cntRooms)
