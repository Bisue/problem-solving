# N과 M 1
# https://study.helloalgo.co.kr/study/1019/room/591/9378

N, M = map(int, input().split())

# used = [False for _ in range(N + 1)]
used = set()


def printPerm(n, m, picks):
    if len(picks) == m:
        print(" ".join(map(str, picks)))
        return

    for i in range(1, n + 1):
        # if not used[i]:
        # used[i] = True
        # picks.append(i)
        # printPerm(n, m, picks)
        # picks.pop()
        # used[i] = False
        if i not in used:
            used.add(i)
            picks.append(i)
            printPerm(n, m, picks)
            picks.pop()
            used.remove(i)


printPerm(N, M, [])
