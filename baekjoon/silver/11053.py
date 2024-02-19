# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

"""
dp[x]: 0~x 가자의 가장 긴 증가하는 부분 수열의 길이
mins[x]: 증가하는 부분 수열의 길이가 x일때, 가장 마지막 수(큰 수)
"""

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N)]
mins = [1e10 for _ in range(N + 1)]
mins[0] = 0

for i in range(N):
    idx = 0
    s, e = 0, N
    while s <= e:
        m = (s + e) // 2
        if mins[m] < nums[i]:
            idx = m
            s = m + 1
        else:
            e = m - 1

    dp[i] = idx + 1
    mins[idx + 1] = nums[i]

print(max(dp))
