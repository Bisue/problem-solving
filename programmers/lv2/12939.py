# 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939

# (github actions 테스트용)


def solution(s):
    nums = list(map(int, s.split()))

    nums.sort()

    return f"{nums[0]} {nums[-1]}"
