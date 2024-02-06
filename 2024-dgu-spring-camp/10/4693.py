# 이분 그래프
# https://study.helloalgo.co.kr/study/1019/room/597/6544

import sys
from collections import deque

V, E = map(int, input().split())
graphs = { v: [] for v in range(1, V+1)}
for _ in range(E):
	a, b = map(int, sys.stdin.readline().rstrip().split())
	
	graphs[a].append(b)
	graphs[b].append(a)
	
tagged = [False for _ in range(V+1)]
tags = [False for _ in range(V+1)]
def tagId(sv):
	q = deque()
	visited = set()
	
	q.append((sv, True))
	visited.add(sv)
	while len(q) > 0:
		cv, ct = q.popleft()
		tags[cv] = ct
		tagged[cv] = True
		
		for nv in graphs[cv]:
			if nv not in visited:
				q.append((nv, not ct))
				visited.add(nv)


for v in range(1, V+1):
	if not tagged[v]:
		tagId(v)

bipartite = True
for s in graphs:
	if not bipartite:
		break
	for e in graphs[s]:
		# print(tags, (s, e), (tags[s], tags[e]), graphs)
		if tags[s] == tags[e]:
			bipartite = False
			break
			
print('YES' if bipartite else 'NO')
