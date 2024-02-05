# 소방서
# https://study.helloalgo.co.kr/study/1019/room/596/6542

import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
roads = { v: [] for v in range(1, N+1) }
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    
    roads[s].append(e)
    roads[e].append(s)

q = deque()
dists = [-1 for _ in range(N+1)]

for _ in range(K):
    s = int(sys.stdin.readline())
    
    q.append(s)
    dists[s] = 0

while len(q) > 0:
    cv = q.popleft()
    
    for nv in roads[cv]:
        if dists[nv] < 0:
            q.append(nv)
            dists[nv] = dists[cv] + 1
            
print('\n'.join(map(str, dists[1:])))
