# 평균이 들어있는 구간 구하기
# https://study.helloalgo.co.kr/study/1019/room/590/9363

N = int(input())
nums = list(map(int, input().split()))

def solution1(N, nums):
	answer = 0
	for i in range(N):
		for j in range(i, N):
			localSum = 0
			candidates = set()
			for k in range(i, j+1):
				localSum += nums[k]
				candidates.add(nums[k])

			if localSum%(j+1-i) != 0:
				continue

			if localSum//(j+1-i) in candidates:
				answer += 1

	print(answer)
	
solution1(N, nums)
