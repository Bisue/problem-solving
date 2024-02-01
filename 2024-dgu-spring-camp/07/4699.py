# 불
# https://study.helloalgo.co.kr/study/1019/room/594/6491

from collections import deque

# 처음 존재하는 불을 모두 큐에 넣은 뒤, 윌리를 마지막에 큐에 넣음(타입 구분)
# 어떤 타입이든 빈공간(.)으로 확산되게끔 BFS(타입 간 visited 공유 - 어차피 윌리가 돌아가는 경우는 없어서 불이 옮겨 붙지 않아도 됨)
# 탈출 조건은 현재 타입이 윌리(@)이고 board 테두리에 위치한 경우

# 정해 1: 불을 먼저 쫙 퍼트려서 불이 붙는 시간을 구하고, 윌리를 이동하면서 불이 붙는 시간보다 빨리 도착하는지에 대한 조건을 추가해서 BFS 돌기 (BFS 2번)
# 정해 2: 내가 한 풀이

dirs = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    board = []
    for _ in range(H):
        board.append(list(input()))
        
    q = deque()
    visited = set()
    
    sx, sy = None, None
    for x in range(H):
        for y in range(W):
            if board[x][y] == '@':
                sx, sy = x, y
            elif board[x][y] == '*':
                q.append((x, y, '*', 1))
    q.append((sx, sy, '@', 1))
    visited.add((sx, sy))
    
    escape = False
    while len(q) > 0:
        cx, cy, ct, cd = q.popleft()
        
        if ct == '@' and (cx == 0 or cx == H-1 or cy == 0 or cy == W-1):
            print(cd)
            escape = True
            break
            
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == '.' and (nx, ny) not in visited:
                q.append((nx, ny, ct, cd + 1))
                visited.add((nx, ny))
                
    if not escape:
        print('IMPOSSIBLE')
    