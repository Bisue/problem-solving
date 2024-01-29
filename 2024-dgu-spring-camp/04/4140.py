# 탑 쌓기
# https://study.helloalgo.co.kr/study/1019/room/591/6460

N, B = map(int, input().split())
blocks = []
for _ in range(N):
    blocks.append(int(input()))

answer = 1e9
used = [False for _ in range(N)]


def dfs(height, start):
    global answer

    # print(height, used)

    if height >= B:
        answer = min(answer, height - B)
        return

    for i in range(start, N):
        if not used[i] and answer > height + blocks[i] - B:
            used[i] = True
            dfs(height + blocks[i], i + 1)
            used[i] = False


dfs(0, 0)
print(answer)
