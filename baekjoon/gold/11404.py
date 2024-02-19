# 플로이드
# https://www.acmicpc.net/problem/11404

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
dists = [[1e10 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dists[i][i] = 0
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    # 문제 조건: a와 b를 연결하는 노선은 하나가 아닐 수 있다.
    #         -> 가장 짧은 노선만 유효
    dists[a - 1][b - 1] = min(dists[a - 1][b - 1], c)

for m in range(N):
    for s in range(N):
        for e in range(N):
            if dists[s][m] + dists[m][e] < dists[s][e]:
                dists[s][e] = dists[s][m] + dists[m][e]

for row in dists:
    print(" ".join(map(str, map(lambda d: d if d < 1e10 else 0, row))))
