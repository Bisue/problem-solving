# 사과 배달
# https://study.helloalgo.co.kr/study/1019/room/600/6571

# PB -> PA1, PA2 dists 계산
# PA1(or PA2) -> PA2(or PA1) dists 계산
# min(PB~PA1 + PA1~PA2, PB~PA2 + PA2~PA1)
# 이때 PA1~PA2 == PA2~PA1 이므로 그냥
# min(PB~PA1, PB~PA2) + PA1~PA2
import heapq as hq
import sys

C, P, PB, PA1, PA2 = map(int, sys.stdin.readline().split())
graph = { v: [] for v in range(1, P+1) }
for _ in range(C):
	p1, p2, d = map(int, sys.stdin.readline().split())
	graph[p1].append((p2, d))
	graph[p2].append((p1, d))

def getDistsFrom(sv):
	global P, graph
	
	pq = []
	dists = [1e10 for _ in range(P+1)]
	
	hq.heappush(pq, (0, sv))
	dists[sv] = 0
	
	while len(pq) > 0:
		cd, cv = hq.heappop(pq)
		if cd > dists[cv]:
			continue
		
		for nv, nd in graph[cv]:
			if cd + nd < dists[nv]:
				hq.heappush(pq, (cd + nd, nv))
				dists[nv] = cd + nd
				
	return dists

pbDists = getDistsFrom(PB)
paDists = getDistsFrom(PA1)

print(min(pbDists[PA1], pbDists[PA2]) + paDists[PA2])
