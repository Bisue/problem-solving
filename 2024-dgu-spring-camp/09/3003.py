# 연구활동 가는 길(S)
# https://study.helloalgo.co.kr/study/1019/room/596/6536

import heapq as hq

N, M = map(int, input().split())
roads = { v: [] for v in range(1, N+1) }
for _ in range(M):
	s, e, w = map(int, input().split())
	
	roads[s].append((w, e))
	if s != e:
		roads[e].append((w, s))

# 1. 다익스트라(우선순위큐)
def solution1():
	pq = []
	dists = [1e10 for _ in range(N+1)]
	hq.heappush(pq, (0, 1))
	dists[1] = 0

	answer = -1
	while len(pq) > 0:
		cd, cv = hq.heappop(pq)
		if cv == N:
			answer = cd
			break
		
		# 시간초과 이유: 중복되서 들어간 경우 현재 기록된 dists랑 검증해줘야 함
		if cd > dists[cv]:
			continue

		for nw, nv in roads[cv]:
			nd = cd + nw
			if nv < dists[nv]:
				hq.heappush(pq, (nd, nv))
				dists[nv] = nd

	return answer

# 2. DFS 완전탐색
def solution2():
	dists = [1e10 for _ in range(N+1)]
	def dfs(cv, cd):
		dists[cv] = min(dists[cv], cd)
		
		for nw, nv in roads[cv]:
			nd = cd + nw
			if nd < dists[nv]:
				dfs(nv, nd)
				
	dists[1] = 0
	dfs(1, 0)
	
	if dists[N] < 1e10:
		return dists[N]
	else:
		return -1
				
		

print(solution1())
# print(solution2())
