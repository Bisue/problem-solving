# 파일 합치기
# https://study.helloalgo.co.kr/study/1019/room/601/6584

# 합친 걸 또 합치면 다음 합칠때도 누적되어 합해짐.
# 결국에 가장 작은 2개씩 계속 합치면 될 듯

# 합칠 때마다 정렬이 필요하므로 min-heap 사용

import heapq as hq
import sys

N = int(input())
sizes = []
for _ in range(N):
	hq.heappush(sizes, int(sys.stdin.readline()))

answer = 0
while len(sizes) >= 2:
	f1 = hq.heappop(sizes)
	f2 = hq.heappop(sizes)
	
	result = f1 + f2
	hq.heappush(sizes, result)
	answer += result
	
print(answer)
