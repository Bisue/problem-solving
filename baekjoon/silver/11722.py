# 가장 긴 감소하는 부분 수열
# https://www.acmicpc.net/problem/11722

N = int(input())
nums = list(map(int, input().split()))

cnts = [1 for _ in range(N)]
maxes = [0 for _ in range(N + 1)]
maxes[0] = 1e10
for i in range(N):
    idx = 0
    s, e = 0, N
    while s <= e:
        m = (s + e) // 2

        if maxes[m] > nums[i]:
            idx = m
            s = m + 1
        else:
            e = m - 1

    maxes[idx + 1] = nums[i]
    cnts[i] = idx + 1

print(max(cnts))
