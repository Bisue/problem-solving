# 징검다리
# https://school.programmers.co.kr/learn/courses/30/lessons/43236

# check: 거리의 최소값이 mid 일때, 바위를 N개(이하로)만 제거할 수 있는가?
# -> true: 거리의 최소값 높이고 정답 마킹
# -> false: 거리의 최소값 낮추고


def check(mid, rocks, n, distance):
    prev = 0
    removed = 0
    for i in range(len(rocks) + 1):
        cur = distance if i == len(rocks) else rocks[i]

        # print(rocks, 'prev:', prev, ', cur:', cur, ', mid:', mid, ', removed:', removed)
        if cur - prev < mid:
            removed += 1
        else:
            prev = cur

    # 문제 오류?: 문제에서는 정확히 n개의 바위를 없애는 방식이라는 설명인데,
    #            그러려면 아래처럼 이분탐색 조건이랑 answer 갱신 조건이 달라야 함.
    #            그런데, 제출해보면 n개 이하로 제거하는 경우가 정답으로 판정됨
    #            ex: 23, [3, 6, 9, 10, 14, 17], 2 -> 3  (3은 제거를 1개만 해야 됨, 2개 하면 최솟값이 3 이상)
    #
    # print(removed <= n, removed == n)
    return removed <= n, removed <= n


def solution(distance, rocks, n):
    rocks.sort()

    start, end = 1, distance
    answer = None
    while start <= end:
        mid = (start + end) // 2

        # print((start, mid, end))
        isPossible, isAnswer = check(mid, rocks, n, distance)
        if isPossible:
            if isAnswer:
                answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer
