# 중량 제한
# https://study.helloalgo.co.kr/study/1019/room/598/6562

from collections import deque
import sys

N, M = map(int, input().split())
graphs = {}
for _ in range(M):
	s, e, lim = map(int, sys.stdin.readline().split())
	if s not in graphs:
		graphs[s] = []
	if e not in graphs:
		graphs[e] = []
	graphs[s].append((e, lim))
	graphs[e].append((s, lim))
	
sv, ev = map(int, input().split())	

def isPossible(weight):
	q = deque()
	visited = set()
	
	q.append(sv)
	visited.add(sv)
	while len(q) > 0:
		cv = q.popleft()
		if cv == ev:
			return True
		
		for nv, lim in graphs[cv]:
			if nv not in visited and weight <= lim:
				q.append(nv)
				visited.add(nv)
				
	return False

start, end = 1, 1000000000
answer = -1
while start <= end:
	mid = (start + end)//2
	
	if isPossible(mid):
		answer = mid
		start = mid+1
	else:
		end = mid-1
		
print(answer)
