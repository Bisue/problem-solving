# 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

# check: 심사 총 시간이 mid 일때, 각 심사관이 심사한 총 인원이 n 이상인가?
# -> true: 총 시간 줄이기 + 정답 저장
# -> false: 총 시간 늘리기


def check(n, times, mid):
    peoples = 0
    for time in times:
        peoples += mid // time

    return peoples >= n


def solution(n, times):
    start, end = 1, n * max(times)
    answer = None
    while start <= end:
        mid = (start + end) // 2

        if check(n, times, mid):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer
