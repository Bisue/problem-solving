# 세모세모
# https://study.helloalgo.co.kr/study/1019/room/603/6605

import sys


def printSemo(semo):
    for row in semo:
        print(row)
    print()


N = int(sys.stdin.readline())
nums = []
sums = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    nums.append(row)
    sums.append([0 for _ in range(i + 1)])

sums.append([0 for _ in range(N + 1)])

for i in range(N):
    for j in range(i + 1):
        sums[i][j] += nums[i][j]
        sums[i + 1][j] = max(sums[i + 1][j], sums[i][j])
        sums[i + 1][j + 1] = max(sums[i + 1][j + 1], sums[i][j])

print(max(sums[N]))
