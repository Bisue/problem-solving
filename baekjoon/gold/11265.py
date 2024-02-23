# 끝나지 않는 파티
# https://www.acmicpc.net/problem/11265

import sys

N, M = map(int, input().split())
adj = []
for _ in range(N):
    adj.append(list(map(int, sys.stdin.readline().split())))


dists = [[1e10 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        dists[i][j] = adj[i][j]

for m in range(N):
    for s in range(N):
        for e in range(N):
            if dists[s][m] + dists[m][e] < dists[s][e]:
                dists[s][e] = dists[s][m] + dists[m][e]

for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().split())

    if dists[s - 1][e - 1] <= t:
        print("Enjoy other party")
    else:
        print("Stay here")
