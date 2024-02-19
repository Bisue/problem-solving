# 평범한 배낭
# https://www.acmicpc.net/problem/12865

"""
dp[x][y]: 1~X 까지의 물건을 y 한도로 채웠을 때 가치의 최댓값

dp[x][y] = max(dp[x-1][y], dp[x-1][y-wx] + vx)
"""

import sys

N, K = map(int, sys.stdin.readline().split())
objs = []
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    objs.append((w, v))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for x in range(1, N + 1):
    for y in range(K + 1):
        dp[x][y] = dp[x - 1][y]
        if y - objs[x - 1][0] >= 0:
            dp[x][y] = max(dp[x][y], dp[x - 1][y - objs[x - 1][0]] + objs[x - 1][1])

print(dp[N][K])
