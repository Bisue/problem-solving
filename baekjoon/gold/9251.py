# LCS
# https://www.acmicpc.net/problem/9251

"""
dp[x][y]: A[:x], B[:y] 까지의 LCS

dp[x][y] = if A[x]==B[y] then dp[x-1][y-1] + 1
           else then max(dp[x-1][y], dp[x][y-1])
"""

import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

lA, lB = len(A), len(B)

dp = [[0 for _ in range(lB + 1)] for _ in range(lA + 1)]
for x in range(1, lA + 1):
    for y in range(1, lB + 1):
        if A[x - 1] == B[y - 1]:
            dp[x][y] = dp[x - 1][y - 1] + 1
        else:
            dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])

print(dp[lA][lB])
