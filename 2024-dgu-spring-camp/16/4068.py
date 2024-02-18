# 2xN 타일링 2
# https://study.helloalgo.co.kr/study/1019/room/603/6599

N = int(input())

dp = [0 for _ in range(N + 2)]
dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    # dp[i-2]는 *3 지만 세로 2개 채우는 경우는 dp[i-1]에 포함됨
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007

print(dp[N])
