# 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898#


def solution(m, n, puddles):
    puddles = set(map(lambda p: (p[1] - 1, p[0] - 1), puddles))

    roadCnts = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    roadCnts[1][1] = 1

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if x == 1 and y == 1:
                continue
            if (x - 1, y - 1) not in puddles:
                roadCnts[x][y] = roadCnts[x - 1][y] + roadCnts[x][y - 1]

    return roadCnts[n][m] % 1_000_000_007
