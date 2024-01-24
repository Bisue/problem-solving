# 오목판단
# https://study.helloalgo.co.kr/study/1019/room/588/6410

board = []
for _ in range(7):
    board.append(input())

dirs = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1),
]


def isValid(x, y):
    return 0 <= x < 7 and 0 <= y < 7


def stretch(x, y, d):
    length = 0
    for i in range(5):
        dx, dy = dirs[d]
        nx, ny = x + dx * i, y + dy * i

        if isValid(nx, ny) and board[nx][ny] == board[x][y]:
            length += 1
        else:
            break

    return length


found = False
for x in range(7):
    if found:
        break
    for y in range(7):
        if found:
            break
        if board[x][y] == ".":
            continue

        lengthes = []
        # 가로
        lengthes.append(stretch(x, y, 0) + stretch(x, y, 1) - 1)
        # 세로
        lengthes.append(stretch(x, y, 2) + stretch(x, y, 3) - 1)
        # 좌상
        lengthes.append(stretch(x, y, 4) + stretch(x, y, 5) - 1)
        # 우상
        lengthes.append(stretch(x, y, 6) + stretch(x, y, 7) - 1)

        for l in lengthes:
            if l >= 5:
                print(board[x][y])
                found = True
                break
if not found:
    print(".")
