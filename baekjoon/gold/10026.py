# 적록색약
# https://www.acmicpc.net/problem/10026

import sys
from collections import deque

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(sys.stdin.readline()))

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def countSections():
    result = 0

    visited = set()

    for x in range(N):
        for y in range(N):
            if (x, y) in visited:
                continue

            result += 1
            ct = board[x][y]

            q = deque()
            q.append((x, y))
            visited.add((x, y))

            while len(q) > 0:
                cx, cy = q.popleft()

                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if (
                        0 <= nx < N
                        and 0 <= ny < N
                        and board[nx][ny] == ct
                        and (nx, ny) not in visited
                    ):
                        q.append((nx, ny))
                        visited.add((nx, ny))

    return result


original = countSections()

for x in range(N):
    for y in range(N):
        if board[x][y] == "G":
            board[x][y] = "R"

converted = countSections()

print(original, converted)
