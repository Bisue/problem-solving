# 동국대에서도 클라이밍을 할 수 있어요
# https://study.helloalgo.co.kr/exam/618/solve/4006

"""
LIS의 좌표 버전?

dp[x]: x번째 홀드를 선택할 때, 0~x번째 홀드까지의 최대 홀드 개수

kx[i]: i개 홀드를 선택할 수 있는 x의 최솟값
ky[i]: i개 홀드를 선택할 수 있는 y의 최솟값

찐풀이:
x좌표로 정렬을 해두면, x는 인덱스가 되버리고
y기준으로 증가하는 부분 수열(이상인 부분 수열)을 구하면 끝이다 그냥.
(내 풀이가 왜 정답으로 가는지는 증명 못하겠음. -> 찐 풀이를 포함하는 개념이라 그런가?)
"""

import sys

N = int(sys.stdin.readline())
holds = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    holds.append((x, y))

holds.sort(key=lambda h: (h[0], h[1]))


def findIdx(arr, thresh):
    idx = 0
    s, e = 0, N
    while s <= e:
        m = (s + e) // 2

        if arr[m] <= thresh:
            idx = m
            s = m + 1
        else:
            e = m - 1
    return idx


dp = [0 for _ in range(N)]
kx = [1e10 for _ in range(N + 1)]
ky = [1e10 for _ in range(N + 1)]
kx[0] = 0
ky[0] = 0
for i in range(N):
    kxIdx, kyIdx = findIdx(kx, holds[i][0]), findIdx(ky, holds[i][1])

    # print('==== cur: ', holds[i])
    # print('before:', kx, ky)
    # print(' kxIdx, kyIdx', kxIdx, kyIdx)

    dp[i] = min(kxIdx, kyIdx) + 1
    kx[kxIdx + 1] = holds[i][0]
    ky[kyIdx + 1] = holds[i][1]

    # print('after:', kx, ky)

print(max(dp))
