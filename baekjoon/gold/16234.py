# 인구 이동
# https://www.acmicpc.net/problem/16234

"""
너무 비효율적으로 짠 듯(2000ms)

심플하게 짜는 법 생각해보자
"""

import sys
from collections import deque

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

N, L, R = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)


def getOpenedGates():
    gates = {(x, y): [] for x in range(N) for y in range(N)}
    visited = set()
    cnt = 0

    for x in range(N):
        for y in range(N):
            visited.add((x, y))

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) in visited:
                    continue

                if (
                    0 <= nx < N
                    and 0 <= ny < N
                    and L <= abs(board[x][y] - board[nx][ny]) <= R
                ):
                    cnt += 1
                    gates[(x, y)].append((nx, ny))
                    gates[(nx, ny)].append((x, y))

    return gates, cnt


def simulate(gates):
    peoples = {}

    q = deque()

    ids = [[0 for _ in range(N)] for _ in range(N)]
    curId = 1
    for x in range(N):
        for y in range(N):
            if ids[x][y] == 0:
                q.append((x, y))
                ids[x][y] = curId

                cnt = 0
                acc = 0
                while len(q) > 0:
                    cx, cy = q.popleft()
                    cnt += 1
                    acc += board[cx][cy]

                    for nx, ny in gates[(cx, cy)]:
                        if ids[nx][ny] == 0:
                            q.append((nx, ny))
                            ids[nx][ny] = curId

                peoples[curId] = acc // cnt
                curId += 1

    # print(ids)

    for x in range(N):
        for y in range(N):
            board[x][y] = peoples[ids[x][y]]


answer = 0
while True:
    gates, gatesCnt = getOpenedGates()
    if gatesCnt == 0:
        break

    simulate(gates)
    answer += 1

print(answer)
