# 내려가기
# https://www.acmicpc.net/problem/2096

"""
메모리 제한이 4MB로 빡빡함.
-> dp 배열을 모두 유지하지 말고, 이전 row만 유지하며 입력 받으면서 처리
"""

import sys

N = int(sys.stdin.readline())
minDp = [0, 0, 0]
maxDp = [0, 0, 0]
for _ in range(N):
    row = tuple(map(int, sys.stdin.readline().split()))

    nextMinDp = [0, 0, 0]
    nextMaxDp = [0, 0, 0]
    for i in range(3):
        pMax, pMin = -1, 1e10
        for j in range(3):
            if abs(i - j) > 1:
                continue

            pMax = max(pMax, maxDp[j])
            pMin = min(pMin, minDp[j])

        nextMaxDp[i] = row[i] + pMax
        nextMinDp[i] = row[i] + pMin

    minDp = nextMinDp
    maxDp = nextMaxDp

print(max(maxDp), min(minDp))
