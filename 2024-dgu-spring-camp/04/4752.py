# 사과 나누기
# https://study.helloalgo.co.kr/study/1019/room/591/6458/source/825672/

N = int(input())
apples = list(map(int, input().split()))

answer = 1e10


def dfs(d, i):
    global answer

    if i == len(apples):
        answer = min(answer, abs(d))
        return 0

    dfs(d + apples[i], i + 1)
    dfs(d - apples[i], i + 1)


dfs(0, 0)
print(answer)
