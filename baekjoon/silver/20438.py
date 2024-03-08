# 출석체크
# https://www.acmicpc.net/problem/20438

import sys

N, K, Q, M = map(int, sys.stdin.readline().split())

sleeps = set(map(int, sys.stdin.readline().split()))
starts = list(map(int, sys.stdin.readline().split()))

attendances = [0 for _ in range(N + 3)]
for s in starts:
    if s in sleeps:
        continue

    mul = 1
    while s * mul < N + 3:
        if s * mul not in sleeps:
            attendances[s * mul] = 1

        mul += 1

# accAttendances[i] = 3 ~ i번 까지 출석하지 못한 학생 수
# a ~ b번 까지 출석하지 못한 학생 수 = accAttendances[b] - accAttendances[a-1]
accAttendances = [0 for _ in range(N + 3)]
for i in range(3, N + 3):
    accAttendances[i] = accAttendances[i - 1] + (1 - attendances[i])

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    print(accAttendances[b] - accAttendances[a - 1])
