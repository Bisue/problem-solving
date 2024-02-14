# 대표 자연수(KOI전국2009_초등부_1)
# https://study.helloalgo.co.kr/study/1019/room/601/6583

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# 1. O(NlogN + 2N)
def solution1():
	# nums 정렬
	nums.sort()
	
	# 정렬된 배열에서 각 숫자의 처음 인덱스, 마지막 인덱스
	numsPos = {}
	for i in range(N):
		n = nums[i]
		if n not in numsPos:
			numsPos[n] = [i, i]
		else:
			numsPos[n][1] = i

	# 정렬된 배열에서의 누적합
	# sums[X] = sum(nums[:X])
	sums = [0 for _ in range(N+1)]
	for i in range(N):
		sums[i+1] = sums[i] + nums[i]

	minDiff = 1e10
	answer = None
	for n in nums:
		# n의 처음 인덱스, 마지막 인덱스
		start, end = numsPos[n]

		# n보다 작은 값들의 diffSum
		prevDiffSums = start*n - sums[start]
		# n보다 큰 값들의 diffSum
		nextDiffSums = (sums[N] - sums[end+1]) - (N-end-1)*n

		# 총 합
		cur = prevDiffSums + nextDiffSums

		if cur < minDiff:
			minDiff = cur
			answer = n

	print(answer)
	
# 2. O(NlogN + 1)
def solution2():
	nums.sort()
	
	if N%2 == 0:
		print(nums[N//2-1])
	else:
		print(nums[N//2])
	
solution2()
