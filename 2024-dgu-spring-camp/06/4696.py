# 엘리베이터
# https://study.helloalgo.co.kr/study/1019/room/593/6483/source/823529/

from collections import deque

N, A, B, U, D = map(int, input().split())

def isValid(floor):
    return 0 <= floor <= N

def findMinimumClicks(N, A, B, U, D):
    q = deque()
    visited = set()
    q.append((A, 0))
    visited.add(A)
    while len(q) > 0:
        cf, cc = q.popleft()
        if cf == B:
            return cc
        
        for nf in [cf - D, cf + U]:
            if isValid(nf) and nf not in visited:
                q.append((nf, cc + 1))
                visited.add(nf)
                
    return -1

clicks = findMinimumClicks(N, A, B, U,D)
if clicks >= 0:
    print(clicks)
else:
    print('use the stairs')
