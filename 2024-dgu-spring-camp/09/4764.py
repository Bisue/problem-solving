# 외판원 순회
# https://study.helloalgo.co.kr/study/1019/room/596/6535

N = int(input())
cities = []
for _ in range(N):
	cities.append(list(map(int, input().split())))

answer = 1e10
visited = [False for _ in range(N)]
def dfs(start, cur, dist):
	global answer
	
	if cur == start and dist > 0:
		found = True
		for chk in visited:
			if not chk:
				found = False
				break
		if found:
			answer = min(answer, dist)
			return
	
	for i in range(N):
		nd = dist + cities[cur][i]
		if cities[cur][i] > 0 and nd <= answer and not visited[i]:
			visited[i] = True
			dfs(start, i, nd)
			visited[i] = False

for v in range(N):
	dfs(v, v, 0)
	
print(answer)
