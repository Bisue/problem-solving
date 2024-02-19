# 증가하는 가장 큰 수열 찾기
# https://study.helloalgo.co.kr/study/1019/room/604/6612

N = int(input())
nums = list(map(int, input().split()))

dp = [nums[i] for i in range(N)]

for i in range(N):
	for j in range(i):
		if nums[i] > nums[j]:
			dp[i] = max(dp[i], dp[j] + nums[i])
			
print(max(dp))
