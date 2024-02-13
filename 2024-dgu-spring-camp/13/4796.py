# 마을 회의
# https://study.helloalgo.co.kr/study/1019/room/600/6574

import sys
import heapq as hq

N, M, X = map(int, sys.stdin.readline().split())
roads = { v: [] for v in range(1, N+1) }
for _ in range(M):
	a, b, w = map(int, sys.stdin.readline().split())
	roads[a].append((b, w))
	
def getDistsFrom(sv, ev=None):
	global N, roads
	
	pq = []
	dists = [1e10 for _ in range(N+1)]
	
	hq.heappush(pq, (0, sv))
	dists[sv] = 0
	while len(pq) > 0:
		cd, cv = hq.heappop(pq)
		if ev is not None and cv == ev:
			return cd
		if cd > dists[cv]:
			continue
			
		for nv, d in roads[cv]:
			if dists[nv] > cd + d:
				hq.heappush(pq, (cd + d, nv))
				dists[nv] = cd + d
	if ev is None:
		return dists
	else:
		return dists[ev]
	
	
distsFromX = getDistsFrom(X)
maxDist = 0
maxTown = 0
for v in range(1, N+1):
	if v == X:
		continue
	
	curDist = getDistsFrom(v, X) + distsFromX[v]
	if curDist > maxDist:
		maxDist = curDist
		maxTown = v

print(maxDist)

