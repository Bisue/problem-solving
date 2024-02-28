# 두 용액
# https://www.acmicpc.net/problem/2470

"""
2 <= N <= 100,000
-1,000,000,000 <= 특성값 <= 1,000,000,000

!! N개의 특성 값은 모두 다름 !!
(만약 같은 값이 있는 문제였으면 별도 처리해줘야함)
"""

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))


def getUpperBound(arr, target, ignore):
    answer = -1

    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2

        if arr[m] <= target:
            if arr[m] != ignore:  # 자기 자신 선택 방지
                answer = m
            s = m + 1
        else:
            e = m - 1

    return answer


def getLowerBound(arr, target, ignore):
    answer = -1

    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2

        if arr[m] >= target:
            if arr[m] != ignore:  # 자기 자신 선택 방지
                answer = m
            e = m - 1
        else:
            s = m + 1

    return answer


answer = [1e10, None, None]

nums.sort()
# print(nums)

for i in range(len(nums)):
    num = nums[i]
    l = getUpperBound(nums, -num, num)
    r = getLowerBound(nums, -num, num)

    # print(num, nums[l] if l >= 0 else None, nums[r] if r >= 0 else None)

    if l >= 0:
        # print(" - l:", abs(num + nums[l]))
        if abs(num + nums[l]) < answer[0]:
            answer[0] = abs(num + nums[l])
            answer[1] = min(num, nums[l])
            answer[2] = max(num, nums[l])
    if r >= 0:
        # print(" - r:", abs(num + nums[r]))
        if abs(num + nums[r]) < answer[0]:
            answer[0] = abs(num + nums[r])
            answer[1] = min(num, nums[r])
            answer[2] = max(num, nums[r])

print(answer[1], answer[2])
