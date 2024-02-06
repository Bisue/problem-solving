# 트리의 부모 찾기
# https://study.helloalgo.co.kr/study/1019/room/597/6549

import sys
from collections import deque

N = int(input())
parents = [-1 for _ in range(N+1)]
tree = { v: [] for v in range(1, N+1) }
for _ in range(N-1):
	a, b = map(int, sys.stdin.readline().rstrip().split())
	
	tree[a].append(b)
	tree[b].append(a)
	
q = deque()
visited = set()

q.append((1, 0))
visited.add(1)
while len(q) > 0:
	cv, pv = q.popleft()
	parents[cv] = pv
	
	for nv in tree[cv]:
		if nv not in visited:
			q.append((nv, cv))
			visited.add(nv)
			
			
for v in range(2, N+1):
	print(parents[v])
