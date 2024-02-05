# 바이러스(KOI지역2004_초등부_3)
# https://study.helloalgo.co.kr/study/1019/room/596/6538

from collections import deque

N = int(input())
M = int(input())
networks = { v: [] for v in range(1, N+1) }
for _ in range(M):
	s, e = map(int, input().split())
	
	networks[s].append(e)
	networks[e].append(s)
	
answer = 0
	
q = deque()
visited = [False for _ in range(N+1)]

q.append(1)
visited[1] = True
while len(q) > 0:
	cv = q.popleft()
	
	answer += 1
	
	for nv in networks[cv]:
		if not visited[nv]:
			q.append(nv)
			visited[nv] = True
			
print(answer - 1)
