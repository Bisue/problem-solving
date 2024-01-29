# 짐 싣기
# https://study.helloalgo.co.kr/study/1019/room/591/6461/source/825772/

C, N = map(int, input().split())
weights = []
for _ in range(N):
    weights.append(int(input()))

answer = 0


def dfs(weight, start):
    global answer

    answer = max(answer, weight)

    for i in range(start, N):
        nw = weight + weights[i]
        if nw <= C:
            dfs(nw, i + 1)


dfs(0, 0)
print(answer)
