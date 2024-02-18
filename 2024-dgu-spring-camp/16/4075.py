# 길 찾기
# https://study.helloalgo.co.kr/study/1019/room/603/6604

import sys

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(sys.stdin.readline().rstrip())

cnts = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
cnts[1][1] = 1 if board[0][0] == "." else 0
for x in range(N):
    for y in range(N):
        if board[x][y] == "*":
            continue
        if board[x - 1][y] == ".":
            cnts[x + 1][y + 1] = (cnts[x + 1][y + 1] + cnts[x][y + 1]) % 1_000_000_007
        if board[x][y - 1] == ".":
            cnts[x + 1][y + 1] = (cnts[x + 1][y + 1] + cnts[x + 1][y]) % 1_000_000_007

print(cnts[N][N])
