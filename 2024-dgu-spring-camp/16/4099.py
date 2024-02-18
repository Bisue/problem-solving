# 계단 게임
# https://study.helloalgo.co.kr/study/1019/room/603/6608

# dp[n, k]: n개의 계단에서 최대 점수

# dp[n][0] = max(dp[n-2]) + cur
# dp[n][1] = dp[n-1][0] + cur

# answer = max(dp[N])

N = int(input())
scores = [0]
for _ in range(N):
    scores.append(int(input()))

dp = [[0, 0] for _ in range(N + 1)]
dp[1][0] = scores[1]
dp[1][1] = 0
for i in range(2, N + 1):
    dp[i][0] = max(dp[i - 2]) + scores[i]
    dp[i][1] = dp[i - 1][0] + scores[i]

print(max(dp[N]))
