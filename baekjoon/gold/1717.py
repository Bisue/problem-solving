# 집합의 표현
# https://www.acmicpc.net/problem/1717

# 유섭's 추가문제(유니온 파인드)

import sys

N, M = map(int, input().split())

def solution1(N, M):
    parents = [i for i in range(N+1)]

    def getRoot(a):
        if parents[a] == a:
            return a

        parents[a] = getRoot(parents[a])
        return parents[a]

    def merge(a, b):
        rootA = getRoot(a)
        rootB = getRoot(b)

        parents[rootB] = rootA

    def check(a, b):
        rootA = getRoot(a)
        rootB = getRoot(b)

        return rootA == rootB

    for _ in range(M):
        command, a, b = map(int, sys.stdin.readline().rstrip().split())

        if command == 0:
            merge(a, b)
        else:
            if check(a, b):
                print('YES')
            else:
                print('NO')

solution1(N, M)
