# 단지번호붙이기
# https://study.helloalgo.co.kr/study/1019/room/592/6469

dirs = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, list(input()))))

danji = 0
answer = [0 for _ in range(N*N)]
def dfs(x, y):
    global answer, dangi
    
    answer[danji] += 1 # count houses
    board[x][y] = 0 # fill visited
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1:
            dfs(nx, ny)

for x in range(N):
    for y in range(N):
        if board[x][y] == 1:
            dfs(x, y)
            danji += 1

print(danji)
for houses in sorted(answer[:danji]):
    print(houses)
