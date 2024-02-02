# 수강신청2(중간고사)
# https://study.helloalgo.co.kr/exam/616/solve/3990

N, M = map(int, input().split())
ids = list(map(int, input().split()))

success = []
for _ in range(N):
	fIds = list(map(int, input().split()))
	success.append(set(fIds[1:]))

answer = N + 1
picks = []
def dfs(start):
	global answer
	
	cur = set()
	for p in picks:
		cur = cur.union(success[p])
	
	found = True
	for i in ids:
		if i not in cur:
			found = False
			break
	
	if found:
		answer = min(answer, len(picks))
		
	if start == N:
		return
	
	for i in range(start, N):
		picks.append(i)
		dfs(i + 1)
		picks.pop()
		
dfs(0)

print(-1 if answer == N + 1 else answer)
