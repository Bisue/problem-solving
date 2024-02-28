# 선분 위의 점
# https://www.acmicpc.net/problem/11663

import sys

N, M = map(int, sys.stdin.readline().split())
points = list(map(int, sys.stdin.readline().split()))

points.sort()


def getUpperBound(arr, target):
    result = -1

    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2

        if arr[m] <= target:
            result = m
            s = m + 1
        else:
            e = m - 1

    return result


def getLowerBound(arr, target):
    result = -1

    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2

        if arr[m] >= target:
            result = m
            e = m - 1
        else:
            s = m + 1

    return result


for _ in range(M):
    l, r = map(int, sys.stdin.readline().split())

    pl, pr = getLowerBound(points, l), getUpperBound(points, r)
    if pl < 0 or pr < 0:
        print(0)
    else:
        print(pr - pl + 1)
