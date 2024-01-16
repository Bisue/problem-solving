# 야근 지수
# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq


def solution(n, works):
    if n >= sum(works):
        return 0

    maxQ = []
    for w in works:
        heapq.heappush(maxQ, -w)

    while n > 0:
        cur = -heapq.heappop(maxQ)
        heapq.heappush(maxQ, -(cur - 1))
        n -= 1

    answer = sum(map(lambda e: e**2, maxQ))

    return answer
