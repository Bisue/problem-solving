# 서강그라운드
# https://www.acmicpc.net/problem/14938

import sys
import heapq as hq

N, M, R = map(int, sys.stdin.readline().split())
# 각 지역별 아이템 수(0-based index)
items = list(map(int, sys.stdin.readline().split()))
# dists[a][b]: a에서 b로 갈 수 있는 최단거리
dists = [[1e10 for _ in range(N + 1)] for _ in range(N + 1)]
for v in range(1, N + 1):
    dists[v][v] = 0

# 양방향 도로 거리 정의
for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().split())

    dists[a][b] = l
    dists[b][a] = l

# 모든 a에서 모든 b까지의 최단거리 계산 (플로이드 워셜)
for m in range(1, N + 1):
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            if dists[s][m] + dists[m][e] < dists[s][e]:
                dists[s][e] = dists[s][m] + dists[m][e]

# 각 출발지역 별로 반경 내 수집 아이템 수 카운팅 & 최대값 갱신
answer = 0
for s in range(1, N + 1):
    gets = 0
    for e in range(1, N + 1):
        if dists[s][e] <= M:
            gets += items[e - 1]
    answer = max(answer, gets)

print(answer)
