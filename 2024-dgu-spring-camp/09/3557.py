# 어부바
# https://study.helloalgo.co.kr/study/1019/room/596/6541

import sys
from collections import deque

A, B, P, N, M = map(int, input().split())
roads = { v: [] for v in range(1, N+1) }
for _ in range(M):
	s, e = map(int, sys.stdin.readline().rstrip().split())
	
	roads[s].append(e)
	roads[e].append(s)

# sv부터 모든 그래프까지의 에너지 소모 반환
# (1칸 이동 당 multiplier 에너지 소모일 때)
def bfs(sv, multiplier):
	q = deque()
	dists = [-1 for _ in range(N+1)]
	
	q.append((sv, 0))
	dists[sv] = 0
	while len(q) > 0:
		cv, cd = q.popleft()
		
		for nv in roads[cv]:
			nd = cd + multiplier
			if dists[nv] < 0:
				q.append((nv, nd))
				dists[nv] = nd
	
	return dists

# 선기, 루시의 모든 정점으로의 에너지 소모
sunkiDists = bfs(1, A)
lucyDists = bfs(2, B)
# 도착점부터 같이 움직일 때 역순으로 모든 정점으로의 에너지 소모
# (= 같이 움직일 때, 모든 정점에서 도착점까지 가는데 남은 에너지 소모)
togetherDists = bfs(N, P)

answer = 1e10
# i번째에서 만난다고 가정한 에너지 소모 총합 계산 & 최소값 갱신
for i in range(1, N+1):
	if sunkiDists[i] < 0 or lucyDists[i] < 0 or togetherDists[i] < 0:
		continue
	cost = sunkiDists[i] + lucyDists[i] + togetherDists[i]
	answer = min(answer, cost)
	
print(answer)

