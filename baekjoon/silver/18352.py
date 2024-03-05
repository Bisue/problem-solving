# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
roads = {v: [] for v in range(1, N + 1)}
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())

    roads[s].append(e)

q = deque()
dists = [-1 for _ in range(N + 1)]

q.append(X)
dists[X] = 0
while len(q) > 0:
    cv = q.popleft()

    for nv in roads[cv]:
        if dists[nv] < 0:
            q.append(nv)
            dists[nv] = dists[cv] + 1

exists = False
for v in range(1, N + 1):
    if dists[v] != K:
        continue

    print(v)

    if not exists:
        exists = True

if not exists:
    print(-1)
