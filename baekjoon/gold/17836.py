# 공주님을 구해라!
# https://www.acmicpc.net/problem/17836

"""
벽 부수고 이동하기 같은 문제?

문제만 보면 뭔가 검을 안 가졌을 때, 가졌을 때를 고려해야해서
다익스트라를 써야 하는 느낌이지만,

방문 체크(visited)의 차원을 하나 늘려 검을 안 가졌을 때, 가졌을 때를 따로 체크하면 됨.
"""

import sys
from collections import deque

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

N, M, T = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

q = deque()
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

q.append((0, 0, 0, 0))  # x, y, dist, sword
visited[0][0][0] = True

answer = 1e10
while len(q) > 0:
    cx, cy, cd, cs = q.popleft()

    if cx == N - 1 and cy == M - 1:
        answer = min(answer, cd)
        # print((cx, cy, cd, cs), answer)
        break

    if board[cx][cy] == 2:
        cs = 1

    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][cs]:
            if cs == 0 and board[nx][ny] == 1:
                continue

            q.append((nx, ny, cd + 1, cs))
            visited[nx][ny][cs] = True

if answer <= T:
    print(answer)
else:
    print("Fail")
