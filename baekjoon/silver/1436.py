# 영화감독 숌
# https://www.acmicpc.net/problem/1436

N = int(input())


def findNum(N):
    answer = 0

    counts = 0
    cur = 666
    while counts < N:
        token = str(cur)
        if token.find("666") > -1:
            answer = cur
            counts += 1

        cur += 1

    return answer


num = findNum(N)

print(num)
