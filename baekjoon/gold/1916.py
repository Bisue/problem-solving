# 최소비용 구하기
# https://www.acmicpc.net/problem/1916

import sys
import heapq as hq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
buses = { v: [] for v in range(1, N+1) }
for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().split())
    
    buses[a].append((b, w))

sv, ev = map(int, sys.stdin.readline().split())

pq = []
dists = [1e10 for _ in range(N+1)]

hq.heappush(pq, (0, sv))
dists[sv] = 0
while len(pq) > 0:
    cd, cv = hq.heappop(pq)
    if cd > dists[cv]:
        continue
    if cv == ev:
        break
    
    for nv, w in buses[cv]:
        nd = cd + w
        if nd < dists[nv]:
            hq.heappush(pq, (nd, nv))
            dists[nv] = nd
    
print(dists[ev])
