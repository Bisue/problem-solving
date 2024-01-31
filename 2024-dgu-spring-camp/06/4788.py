# 우유 담기
# https://study.helloalgo.co.kr/study/1019/room/593/6484/source/823534/

from collections import deque

X, Y, K, M = map(int, input().split())

minDiff = 1e10

q = deque()
q.append((X, 0, 1))
q.append((0, Y, 1))
# tires[x][y] = (x, y)에 도달한 최소 시행횟수
# => (x, y)에 더 높은 시행횟수로 다시 방문할 필요는 없음
tries = [[1e10 for _ in range(Y+1)] for _ in range(X+1)]
while len(q) > 0:
    cx, cy, ck = q.popleft()
    
    minDiff = min(minDiff, abs(M - (cx + cy)))
    
    if ck == K:
        continue
    # 1. 두 양동이 중 하나 가득 채우기
    nx, ny, nk = X, cy, ck+1
    if cx < X and tries[nx][ny] > nk:
        q.append((nx, ny, nk))
        tries[nx][ny] = nk
    nx, ny, nk = cx, Y, ck+1
    if cy < Y and tries[nx][ny] > nk:
        q.append((nx, ny, nk))
        tries[nx][ny] = nk
    # 2. 두 양동이 중 하나 완전히 비우기
    nx, ny, nk = 0, cy, ck+1
    if cx > 0 and tries[nx][ny] > nk:
        q.append((nx, ny, nk))
        tries[nx][ny] = nk
    nx, ny, nk = cx, 0, ck+1
    if cy > 0 and tries[nx][ny] > nk:
        q.append((nx, ny, nk))
        tries[nx][ny] = nk
    # 3. x -> y 가득 찰 때까지
    amount = min(cx, Y - cy)
    nx, ny, nk = cx - amount, cy + amount, ck+1
    if cx > 0 and cy < Y and tries[nx][ny] > nk:
        q.append((nx, ny, nk))
        tries[nx][ny] = nk
    # 4. y -> x 가득 찰 때까지
    amount = min(cy, X - cx)
    nx, ny, nk = cx + amount, cy - amount, ck+1
    if cx < X and cy > 0 and tries[nx][ny] > nk:
        q.append((nx, ny, nk))
        tries[nx][ny] = nk
    
print(minDiff)
