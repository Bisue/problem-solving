# 연결 요소의 개수
# https://study.helloalgo.co.kr/study/1019/room/596/6539

import sys
from collections import deque

sys.setrecursionlimit(10000)

N, M = map(int, input().split())
graph = { v: [] for v in range(1, N+1) }
for _ in range(M):
	# input(): M이 크면 입력 시간초과 날 수 있음.
	s, e = map(int, sys.stdin.readline().rstrip().split())
	
	graph[s].append(e)
	graph[e].append(s)

visited = set()
def dfs(cur):
	visited.add(cur)
	
	for nv in graph[cur]:
		if nv not in visited:
			dfs(nv)

answer = 0
for v in graph:
	if v in visited:
		continue
	
	dfs(v)
	answer += 1

print(answer)
