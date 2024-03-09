# 회전 초밥
# https://www.acmicpc.net/problem/15961

import sys

N, D, K, C = map(int, sys.stdin.readline().split())
belt = []
for _ in range(N):
    belt.append(int(sys.stdin.readline()))

for i in range(K):
    belt.append(belt[i])

picks = 0

count = [0 for _ in range(D + 1)]
count[C] = 1  # bonus coupon
picks += 1

s, e = 0, K
for i in range(s, e):
    if count[belt[i]] == 0:
        picks += 1
    count[belt[i]] += 1

answer = picks
while e < N + K:
    count[belt[s]] -= 1
    if count[belt[s]] == 0:
        picks -= 1

    count[belt[e]] += 1
    if count[belt[e]] == 1:
        picks += 1

    s, e = s + 1, e + 1
    answer = max(answer, picks)

print(answer)
