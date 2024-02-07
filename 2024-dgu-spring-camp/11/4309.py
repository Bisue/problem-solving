# 케이블 자르기
# https://study.helloalgo.co.kr/study/1019/room/598/6556

import sys

N, M = map(int, input().split())
cables = []
for _ in range(N):
	cables.append(int(sys.stdin.readline()))

start, end = 1, max(cables)
answer = -1
while start <= end:
	mid = (start + end)//2
	
	newCables = 0
	for cable in cables:
		newCables += cable//mid
		
	if newCables >= M:
		answer = mid
		start = mid + 1
	else:
		end = mid - 1
print(answer)
