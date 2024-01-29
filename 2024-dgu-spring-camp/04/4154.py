# 모든 순열
# https://study.helloalgo.co.kr/study/1019/room/591/9377/source/825643/

N = int(input())

used = [False for _ in range(N + 1)]


def printPerm(n, picks):
    if len(picks) == n:
        print(" ".join(map(str, picks)))
        return

    start = 1 if len(picks) == 0 else picks[-1] + 1
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            picks.append(i)
            printPerm(n, picks)
            picks.pop()
            used[i] = False


printPerm(N, [])
