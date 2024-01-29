# 양팔 저울
# https://study.helloalgo.co.kr/study/1019/room/591/6459/source/825771/

N = int(input())
weights = list(map(int, input().split()))

used = [False for _ in range(N)]
possible = set()


def dfs(num, start, pickCnt):
    global answer

    if pickCnt == N:
        return

    possible.add(num)

    for i in range(start, N):
        if not used[i]:
            used[i] = True
            dfs(num + weights[i], i + 1, pickCnt + 1)
            used[i] = False


dfs(0, 0, 0)
print(len(possible))
