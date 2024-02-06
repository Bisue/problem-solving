# 우유 공장
# https://study.helloalgo.co.kr/study/1019/room/597/6547

N = int(input())
roads = { v: [] for v in range(1, N+1) }
for _ in range(N-1):
	p, q = map(int, input().split())
	
	roads[p].append(q)
	
connected = [0 for _ in range(N+1)]

def fillCount(cv, visited):
	if cv in visited:
		return
	
	visited.add(cv)
	connected[cv] += 1
	for nv in roads[cv]:
		fillCount(nv, visited)
		
for v in range(1, N+1):
	fillCount(v, set())
	
answer = -1
for v in range(1, N+1):
	if connected[v] == N:
		answer = v
		
print(answer)
