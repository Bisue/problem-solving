# 겹치는 건 싫어
# https://www.acmicpc.net/problem/20922

import sys

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

answer = 0

s, e = 0, 0
count = [0 for _ in range(100_001)]
while s <= e and e < N:
    if count[nums[e]] >= K:
        count[nums[s]] -= 1
        s += 1
    else:
        count[nums[e]] += 1
        e += 1

    answer = max(answer, e - s)

print(answer)
