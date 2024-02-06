# 서브트리 노드 수 구하기
# https://study.helloalgo.co.kr/study/1019/room/597/6550

import sys
from collections import deque

sys.setrecursionlimit(1000000)

N, R, Q = map(int, input().split())
tree = {v: [] for v in range(1, N+1)}
for _ in range(N-1):
	u, v = map(int, sys.stdin.readline().rstrip().split())
	
	tree[u].append(v)
	tree[v].append(u)
#

cache = {v: -1 for v in tree}
visited = set()
def countSubtreeNodes(cv):
	if cache[cv] >= 0:
		return cache[cv]
	
	visited.add(cv)
	
	nodes = 1
	for nv in tree[cv]:
		if nv not in visited:
			nodes += countSubtreeNodes(nv)
			
	cache[cv] = nodes
	return nodes

visited.add(R)
countSubtreeNodes(R)

#
for _ in range(Q):
	u = int(sys.stdin.readline().rstrip())
	
	visited = set([u])
	print(countSubtreeNodes(u))
	
	