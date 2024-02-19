# 스티커
# https://www.acmicpc.net/problem/9465

"""
풀었지만 정해는 아닌 것 같음.

내 풀이:
dp[x][y]: dp[:][:y+1] 범위에서 (x, y) 스티커를 사용했을 때 최댓값
dp[x][y] = dp[x][y] + max(가능한 이전까지의 최댓값...)

이때 max(가능한 이전까지의 최댓값...) 부분을 O(1)에 찾기 위해서
maxes 변수를 도입함
maxes: 현재까지 점수의 가장 큰 3개를 보관. (점수 + pos(x, y) 보관)

3개를 계속 업데이트하면서 유지하면, dp[x][y] 에서 점수의 최댓값을 결정할 때
maxes 3개 중 (x, y)와 같이 사용할 수 있는 pos를 꺼내서 쓰면 됨.

check: if (mp[0] == pos[0] and mp[1] < pos[1] - 1)
          or (mp[0] != pos[0] and mp[1] < pos[1])
"""

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    dp = []
    for _ in range(2):
        dp.append(list(map(int, sys.stdin.readline().split())))

    maxes = [(-1, None), (-1, None), (-1, None)]

    def updateMaxes(val, pos):
        if val > maxes[0][0]:
            maxes[2] = maxes[1]
            maxes[1] = maxes[0]
            maxes[0] = (val, pos)
        elif val > maxes[1][0]:
            maxes[2] = maxes[1]
            maxes[1] = (val, pos)
        elif val > maxes[2][0]:
            maxes[2] = (val, pos)

    def getMax(pos):
        for i in range(3):
            mv, mp = maxes[i]
            if mp[0] == pos[0] and mp[1] < pos[1] - 1:
                return mv
            elif mp[0] != pos[0] and mp[1] < pos[1]:
                return mv

    for i in range(2):
        updateMaxes(dp[i][0], (i, 0))

    for j in range(1, N):
        for i in range(2):
            dp[i][j] += getMax((i, j))

            updateMaxes(dp[i][j], (i, j))

    print(max(dp[0][N - 1], dp[1][N - 1]))
