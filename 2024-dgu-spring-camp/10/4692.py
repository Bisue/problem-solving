# 등수 찾기
# https://study.helloalgo.co.kr/study/1019/room/597/6548

import sys

N, M, X = map(int, input().split())
wins = { v: [] for v in range(1, N+1) }
loses = { v: [] for v in range(1, N+1) }
for _ in range(M):
	a, b = map(int, sys.stdin.readline().rstrip().split())
	
	wins[a].append(b)
	loses[b].append(a)
	
def getBattleInfoOf(visited, sv, cv, win = True):
	if cv in visited:
		return 0
	
	targets = wins[cv] if win else loses[cv]
	visited.add(cv)
	
	ops = 0 if cv == sv else 1
	for nv in targets:
		ops += getBattleInfoOf(visited, sv, nv, win=win)
		
	return ops

xWins = getBattleInfoOf(set(), X, X)
xLoses = getBattleInfoOf(set(), X, X, win=False)

# 5명 있는데 4명을 이겼어 -> 무조건 1등
# 5명 있는데 3명을 이겼어 -> 1등 or 2등
# 5명 있는데 2명을 이겼어 -> 1등 or 2등 or 3등
# 5명 있는데 1명을 이겼고 2명한테 졌어 -> 최저 4등, 최고 3등 -> 3등 or 4등
print(1+xLoses, N-xWins)
