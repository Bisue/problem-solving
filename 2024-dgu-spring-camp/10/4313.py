# 키 순서
# https://study.helloalgo.co.kr/study/1019/room/597/6546

# 결국 그래프에서, 자신의 간선을 따라 쭈욱 갔을 때 모든 노드를 돌 수 있으면 나의 순서를 알 수 있음
# 근데 자신을 가리키는 간선도 살펴봐야함

import sys

N, M = map(int, input().split())
graphs = { v: [] for v in range(1, N+1) }
revGraphs = { v: [] for v in range(1, N+1) }
for _ in range(M):
	a, b = map(int, sys.stdin.readline().rstrip().split())
	
	graphs[a].append(b)
	revGraphs[b].append(a)
	
def countLinkedNodes(cv, visited, reverse=False):
	if cv in visited:
		return 0
	
	linked = revGraphs[cv] if reverse else graphs[cv]
	visited.add(cv)
	
	nodes = 1
	for nv in linked:
		nodes += countLinkedNodes(nv, visited, reverse)
		
	return nodes

answer = 0
for v in range(1, N+1):
	forward = countLinkedNodes(v, set())
	backward = countLinkedNodes(v, set(), reverse=True)
	result = forward + backward - 1
	
	if result == N:
		answer += 1

print(answer)
