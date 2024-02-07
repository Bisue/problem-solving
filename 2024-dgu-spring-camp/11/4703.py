# 동전 금고
# https://study.helloalgo.co.kr/study/1019/room/598/6561/source/828430/

# 높이가 x인 사다리를 가진 채 동전을 찾을 수 있는가?
from collections import deque

dirs = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    
def isPossible(ladder):
    q = deque()
    visited = set()
    
    q.append((0, 0))
    visited.add((0, 0))
    while len(q) > 0:
        cx, cy = q.popleft()
        if cx == N-1 and cy == M-1:
            return True
        
        for dx, dy in dirs:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<M and board[cx][cy] + ladder >= board[nx][ny] and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
                
    return False
    
start, end = 0, 1_000_000_000
answer = -1
while start <= end:
    mid = (start + end)//2
    
    if isPossible(mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
        
print(answer)
