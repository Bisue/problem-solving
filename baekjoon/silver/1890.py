# 점프
# https://www.acmicpc.net/problem/1890

N = int(input())

board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
for x in range(N):
    for y in range(N):
        if dp[x][y] == 0 or board[x][y] == 0:
            continue

        # print('- ', (x, y))

        nx, ny = x + board[x][y], y + board[x][y]
        if nx < N:
            # print((nx, y), dp[nx][y], '->', dp[nx][y] + dp[x][y])
            dp[nx][y] += dp[x][y]
        if ny < N:
            # print((x, ny), dp[x][ny], '->', dp[x][ny] + dp[x][y])
            dp[x][ny] += dp[x][y]

# for row in dp:
#     print(row)
print(dp[N - 1][N - 1])
