# 입국심사
# https://www.acmicpc.net/problem/3079

"""
기다렸다가 이동이 가능하다?
-> 쓸데없이 놀고 있는 심사원이 없다

이분탐색
- 심사를 받는데 걸리는 시간이 x이고,
  이 시간 동안 n명의 모든 심사원이 놀지 않고 일을 할 때,
  m명 이상을 심사할 수 있는가?
  
1e18 why?
- 가능한 시간의 최댓값은 N이 1이고 M이 1e9, T1 = 1e9 일때 T1*M == 1e18 이다.
"""

import sys

N, M = map(int, input().split())
officers = []
for _ in range(N):
    officers.append(int(sys.stdin.readline()))


def check(time):
    peoples = 0
    for officer in officers:
        peoples += time // officer

    return peoples >= M


answer = 0

s, e = 0, 1e18
while s <= e:
    m = int((s + e) // 2)

    if check(m):
        answer = m
        e = m - 1
    else:
        s = m + 1

print(answer)
