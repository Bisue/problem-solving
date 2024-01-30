# 다이어트
# https://study.helloalgo.co.kr/study/1019/room/592/6476

N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingredients = []
for _ in range(N):
	p, f, s, v, c = map(int, input().split())
	ingredients.append((p, f, s, v, c))

picks = []
answer = [1e10, []]
def dfs(start, p, f, s, v, c):
	global picks, answer
	
	if len(picks) == N:
		return
	if p >= mp and f >= mf and s >= ms and v >= mv and answer[0] > c:
		answer = [c, list(picks)]
		return
	
	for i in range(start, N):
		cp, cf, cs, cv, cc = ingredients[i]
		picks.append(i)
		dfs(i+1, p+cp, f+cf, s+cs, v+cv, c+cc)
		picks.pop()

dfs(0, 0, 0, 0, 0, 0)
print(answer[0])
print(' '.join(map(str, map(lambda n: n+1, answer[1]))))
