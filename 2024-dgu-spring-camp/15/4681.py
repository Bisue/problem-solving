# 좌표 압축
# https://study.helloalgo.co.kr/study/1019/room/602/6597

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
sortedNums = sorted(nums)

counts = {}
kind = 0
for i in range(N):
	if sortedNums[i] not in counts:
		counts[sortedNums[i]] = kind
		kind += 1

for num in nums:
	print(counts[num], end=' ')
print()
