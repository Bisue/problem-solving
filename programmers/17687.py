# [3차] n진수 게임 (2018 KAKAO BLIND RECRUITMENT)
# https://school.programmers.co.kr/learn/courses/30/lessons/17687

from collections import deque


def convert(num, n):
    strs = deque()
    if num == 0:
        strs.append("0")

    while num > 0:
        digit = num % n
        if digit < 10:
            digit = str(digit)
        else:
            digit = chr(ord("A") + (digit - 10))

        strs.appendleft(digit)
        num //= n

    return "".join(strs)


def solution(n, t, m, p):
    mines = []
    buffer = deque()

    turn = 0
    num = 0
    while len(mines) < t:
        if len(buffer) == 0:
            digits = list(convert(num, n))

            for digit in digits:
                buffer.append(digit)

            num += 1

        now = buffer.popleft()

        if turn % m == p - 1:
            mines.append(now)

        turn += 1

    return "".join(mines)
