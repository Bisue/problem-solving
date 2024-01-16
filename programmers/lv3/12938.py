# 최고의 집합
# https://school.programmers.co.kr/learn/courses/30/lessons/12938

"""
곱이 가장 크려면 중복집합 내 숫자가 고른 크기를 가져야 함.
== 타겟 넘버 n을 s로 나눈 몫을 집합에 쭈욱 뿌리고
   나머지를 1씩 분배하면 됨.
   (n을 s로 나눈 몫이 0인 경우는 자연수가 아닌 원소가
   존재하게 되므로 정답이 없음)
"""


def solution(n, s):
    minimum = s // n
    remained = s % n

    if minimum == 0:
        return [-1]

    answer = [minimum for _ in range(n)]
    for i in range(remained):
        answer[n - i - 1] += 1

    return answer
