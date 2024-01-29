# N과 M 3
# https://study.helloalgo.co.kr/study/1019/room/591/6456/source/825523/

N, M = map(int, input().split())


def printPerm(n, m, picks):
    if len(picks) == m:
        print(" ".join(map(str, picks)))
        return

    for num in range(1, n + 1):
        picks.append(num)
        printPerm(n, m, picks)
        picks.pop()


printPerm(N, M, [])
