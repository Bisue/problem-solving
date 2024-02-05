# 촌수계산
# https://study.helloalgo.co.kr/study/1019/room/596/6540

from collections import deque

N = int(input())
sv, ev = map(int, input().split())
M = int(input())

jokbo = { v: [] for v in range(1, N+1)  } # 부모든 자식이든 1촌인 것은 동일하므로 촌수만 계산하는 경우 동일하게 간주 가능
for _ in range(M):
	s, e = map(int, input().split())
	
	jokbo[s].append(e)
	jokbo[e].append(s)
	
q = deque()
visited = set()

q.append((sv, 0))
visited.add(sv)

answer = -1
while len(q) > 0:
	cv, cc = q.popleft()
	if cv == ev:
		answer = cc
		break
		
	for nv in jokbo[cv]:
		if nv not in visited:
			q.append((nv, cc+1))
			visited.add(nv)

print(answer)
