# 통행료
# https://study.helloalgo.co.kr/study/1019/room/600/6570

import heapq as hq
import sys

N, M = map(int, sys.stdin.readline().split())
roads = { v: [] for v in range(1, N+1) }
for _ in range(M):
	a, b, c = map(int, sys.stdin.readline().split())
	roads[a].append((b, c))
	roads[b].append((a, c))
	
cows = [1e10 for _ in range(N+1)]
pq = []

cows[1] = 0
hq.heappush(pq, (0, 1))

while len(pq) > 0:
	cc, cv = hq.heappop(pq)
	if cv == N:
		break
	if cc > cows[cv]:
		continue
		
	for nv, c in roads[cv]:
		if cows[nv] > cc + c:
			hq.heappush(pq, (cc + c, nv))
			cows[nv] = cc + c

print(cows[N])
