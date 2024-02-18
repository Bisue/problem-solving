# 용돈받는 윌리
# https://study.helloalgo.co.kr/study/1019/room/603/6607

import sys

N = int(sys.stdin.readline())

dp = []
for _ in range(N):
    pay = list(map(int, sys.stdin.readline().split()))
    dp.append(pay)

for i in range(1, N):
    for j in range(3):
        prevMax = 0
        for prevJ in range(3):
            if j == prevJ:
                continue

            prevMax = max(prevMax, dp[i - 1][prevJ])

        dp[i][j] = dp[i][j] + prevMax

print(max(dp[N - 1]))
