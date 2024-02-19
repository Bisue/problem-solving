# 공통 부분 문자열
# https://www.acmicpc.net/problem/5582

"""
dp[x][y]: A[x-1]와 B[y-1]를 꼭 포함하면서, A[:x], B[:y] 까지의 가장 긴 공통 부분 문자열 길이
(0<=x<len(A)+1, 0<=y<len(B)+1)
dp[x][y] = if A[x-1]==B[y-1] then dp[x-1][y-1] + 1
           else then 0
"""

A = input()
B = input()

lA, lB = len(A), len(B)

answer = 0
dp = [[0 for _ in range(lB + 1)] for _ in range(lA + 1)]
for x in range(1, lA + 1):
    for y in range(1, lB + 1):
        if A[x - 1] == B[y - 1]:
            dp[x][y] = dp[x - 1][y - 1] + 1
        else:
            dp[x][y] = 0
        answer = max(answer, dp[x][y])

print(answer)
