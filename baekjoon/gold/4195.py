# 친구 네트워크
# https://www.acmicpc.net/problem/4195

# 유섭's 추가문제(유니온 파인드)

import sys

sys.setrecursionlimit(200000)

T = int(input())
for _ in range(T):
    F = int(sys.stdin.readline())
    bestFriend = {}
    networkSizes = {}

    def find(name):
        if bestFriend[name] == name:
            return name

        bestFriend[name] = find(bestFriend[name])
        return bestFriend[name]

    def union(name1, name2):
        rt1 = find(name1)
        rt2 = find(name2)

        # 같을 경우 예외처리 (카운트 덧셈 로직이 있어서 필수)
        if rt1 == rt2:
            return networkSizes[rt1]

        bestFriend[rt2] = rt1
        size = networkSizes[rt1] + networkSizes[rt2]
        networkSizes[rt1] = size
        networkSizes[rt2] = size

        return size

    for _ in range(F):
        n1, n2 = sys.stdin.readline().split()
        if n1 > n2:
            n1, n2 = n2, n1

        if n1 not in bestFriend:
            bestFriend[n1] = n1
            networkSizes[n1] = 1
        if n2 not in bestFriend:
            bestFriend[n2] = n2
            networkSizes[n2] = 1

        print(union(n1, n2))
