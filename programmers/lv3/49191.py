# 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/49191

from collections import deque


def getCount(graph, sv):
    q = deque([sv])
    visited = {sv}

    result = 0
    while len(q) > 0:
        cv = q.popleft()

        result += 1
        for nv in graph[cv]:
            if nv not in visited:
                q.append(nv)
                visited.add(nv)

    return result - 1  # 본인 제외


def solution(n, results):
    wins = {v: [] for v in range(1, n + 1)}
    losses = {v: [] for v in range(1, n + 1)}
    for w, l in results:
        wins[w].append(l)
        losses[l].append(w)

    answer = 0
    for v in range(1, n + 1):
        # 내가 확실하게 이기는 사람 카운팅
        win = getCount(wins, v)
        # 내가 확실하게 지는 사람 카운팅
        lose = getCount(losses, v)
        # 확실하게 아는 사람 수
        knowns = win + lose + 1

        if knowns == n:
            answer += 1

    return answer
