# 밧줄
# https://study.helloalgo.co.kr/study/1019/room/601/6581

"""
로프 중량제한을 내림차순으로 정렬한 뒤,
큰 순으로 N개를 사용하면,
마지막으로 사용한 로프(사용한 로프 중 가장 약한 로프)*N이 최대 중량
"""

import sys

N = int(sys.stdin.readline())
ropes = []
for _ in range(N):
	ropes.append(int(sys.stdin.readline()))
	
ropes.sort(reverse=True)

answer = 0
for i in range(N):
	usedCnt = i + 1
	
	answer = max(answer, usedCnt*ropes[i])

print(answer)
