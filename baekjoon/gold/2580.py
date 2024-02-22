# 스도쿠
# https://www.acmicpc.net/problem/2580

board = []
for _ in range(9):
    board.append(list(map(int, input().split())))


# 현재 board[x][y]에서 가능한 숫자
def getPossibles(x, y):
    possibles = set([i for i in range(1, 10)])
    # 가로
    for i in range(9):
        if board[x][i] in possibles:
            possibles.remove(board[x][i])
    # 세로
    for i in range(9):
        if board[i][y] in possibles:
            possibles.remove(board[i][y])
    # 3x3
    sx, sy = (x // 3) * 3, (y // 3) * 3
    for i in range(sx, sx + 3):
        for j in range(sy, sy + 3):
            if board[i][j] in possibles:
                possibles.remove(board[i][j])

    return list(possibles)


# 스도쿠 풀이 찾았는지 여부
found = False


def dfs(points, i):
    global found

    # 다 채웠으면(모두 숫자를 넣을 수 있으면)
    # 찾았다고 표시 후 출력
    if i >= len(points):
        found = True
        for x in range(9):
            for y in range(9):
                print(board[x][y], end=" ")
            print()
        return

    # 이미 찾았으면 더 돌릴 필요 없음(답은 유일)
    if found:
        return

    cx, cy = points[i]
    # 현재 point에서 가능한 숫자 모두 넣어보기
    for num in getPossibles(cx, cy):
        board[cx][cy] = num
        dfs(points, i + 1)
        board[cx][cy] = 0


# 넣어야 하는 points 추출
points = []
for x in range(9):
    for y in range(9):
        if board[x][y] == 0:
            points.append((x, y))

dfs(points, 0)
# 모든 경우의 수 돌려봐도 숫자를 모두 못채웠으면
# 불가능한 문제
if not found:
    print("Not Possible")
