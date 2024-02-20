# 가장 큰 증가하는 부분 수열
# https://www.acmicpc.net/problem/11055

N = int(input())
nums = list(map(int, input().split()))

dp = [nums[i] for i in range(N)]

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])

print(max(dp))
