# N과 M 2
# https://study.helloalgo.co.kr/study/1019/room/591/9376/source/825546/

N, M = map(int, input().split())


def printPerm(n, m, picks):
    if len(picks) == m:
        print(" ".join(map(str, picks)))
        return

    start = 1 if len(picks) == 0 else picks[-1] + 1
    for num in range(start, n + 1):
        picks.append(num)
        printPerm(n, m, picks)
        picks.pop()


printPerm(N, M, [])
