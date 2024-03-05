# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

import sys

sys.setrecursionlimit(200000)

N = int(sys.stdin.readline())

graphs = {v: [] for v in range(1, N + 1)}
for _ in range(N - 1):
    s, e = map(int, sys.stdin.readline().split())
    graphs[s].append(e)
    graphs[e].append(s)

parents = [0 for _ in range(N + 1)]
parents[1] = 1


def markParent(parent):
    global parents

    print("cur: ", parent)

    for child in graphs[parent]:
        if parents[child] == 0:
            parents[child] = parent
            markParent(child)


markParent(1)

for i in range(2, N + 1):
    print(parents[i])
