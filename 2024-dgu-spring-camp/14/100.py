# 배식
# https://study.helloalgo.co.kr/study/1019/room/601/6578

# i 번째 사람이 식판을 받는 시간
# = i-1 번째까지 식판을 받는데 필요한 시간의 합
# 결국 합의 최솟값을 구하려면, 오름차순으로 서야 함

import sys

N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

times.sort()

answer = 0
acc = 0
for i in range(N):
	now = acc + times[i]
	answer += now
	
	# print(f'i({i}), acc({acc}), now({now}), answer({answer})')
	
	acc = now
	
print(answer)
