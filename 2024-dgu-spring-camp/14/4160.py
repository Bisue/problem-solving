# 윌리의 시간관리
# https://study.helloalgo.co.kr/study/1019/room/601/6585

# i번째 일의 실제 데드라인은 (i+1번째 일의 실제 데드라인 - i+1번째 일의 소요시간) 임.
# 주어진 데드라인을 기준으로 정렬한 뒤,
# 가장 늦은 데드라인에서부터 실제 데드라인을 전파
# 모두 전파되면 가장 빠른 데드라인을 가진 일을 기준으로 일의 시작시간 계산
# (음수면 -1)

import sys

N = int(input())
works = []
for _ in range(N):
	T, S = map(int, sys.stdin.readline().split())
	works.append([T, S])

works.sort(key=lambda w: w[1], reverse=True)

for i in range(1, N):
	realDeadline = works[i-1][1] - works[i-1][0]
	works[i][1] = min(works[i][1], realDeadline)
	
print(max(-1, works[-1][1] - works[-1][0]))
