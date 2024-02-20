# 형스킨라빈스 주니원 배달 주문
# https://study.helloalgo.co.kr/exam/618/solve/4005

"""
형준아이스
- 크기 C -> C분
- 실내 들어가면 C 초기화
  (결국 도로의 길이가 C 이하여야 함)

가능한 작은 크기
-> 이분탐색 + 다익스트라?

"""

import sys
import heapq

N, M, T = map(int, sys.stdin.readline().split())
roads = {v: [] for v in range(1, N + 1)}
roadMax = 0
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    roads[a].append((b, c))
    roads[b].append((a, c))
    roadMax = max(roadMax, c)


def check(ice):
    pq = []
    dists = [1e10 for _ in range(N + 1)]
    heapq.heappush(pq, (0, 1))
    dists[1] = 0

    while len(pq) > 0:
        cd, cv = heapq.heappop(pq)
        if cd > dists[cv]:
            continue

        for nv, l in roads[cv]:
            if l <= ice and cd + l < dists[nv]:
                heapq.heappush(pq, (cd + l, nv))
                dists[nv] = cd + l

    return dists[N] <= T


answer = 0
s, e = 0, roadMax + 1
while s <= e:
    m = (s + e) // 2

    if check(m):
        answer = m
        e = m - 1
    else:
        s = m + 1

print(answer)
