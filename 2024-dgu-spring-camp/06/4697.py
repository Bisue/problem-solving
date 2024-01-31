# 포탈
# https://study.helloalgo.co.kr/study/1019/room/593/6485/source/826096/

from collections import deque

X, Y = map(int, input().split())
q = deque()
visited = [False for _ in range(2*max(X, Y) + 1)]

q.append((X, 0))
visited[X] = True
while len(q) > 0:
    curNum, curCnt = q.popleft()
    
    if curNum == Y:
        print(curCnt)
        break
    
    for nextNum in [curNum+1, curNum-1, 2*curNum]:
        if 0 <= nextNum < 2*max(X, Y) + 1 and not visited[nextNum]:
            q.append((nextNum, curCnt + 1))
            visited[nextNum] = True
