# N-QUEEN 일까?
# https://study.helloalgo.co.kr/study/1019/room/588/6409

dirs = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

n = int(input())
board = []
for i in range(n):
    board.append(input())


def isValid(x, y):
    return 0 <= x < n and 0 <= y < n


def solution():
    queens = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == "Q":
                queens.append((x, y))

    for x, y in queens:
        for dx, dy in dirs:
            for l in range(1, n):
                nx, ny = x + dx * l, y + dy * l
                if isValid(nx, ny) and board[nx][ny] == "Q":
                    return "No"

    return "Yes"


print(solution())
