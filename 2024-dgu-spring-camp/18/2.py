# 젠가의 신
# https://study.helloalgo.co.kr/exam/618/solve/4003

"""
정해는 다른 방식이었음.

PDF 참고
"""

import sys
import heapq

"""
2 5 1 4 3
5 1 4 3 2
5 1 4 2 3
5 1 2 3 4
1 2 3 4 5

1 5 7 3 8 2 6 4
1 5 7 8 2 6 4 3
1 5 7 8 2 6 3 4
1 7 8 2 6 3 4 5
1 7 8 2 3 4 5 6
1 8 2 3 4 5 6 7
1 2 3 4 5 6 7 8
"""

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
pq = []
for i in range(N):
    heapq.heappush(pq, (nums[i], i))

accIdx = N
prev = -1
answer = 0
while len(pq) > 0:
    num, idx = heapq.heappop(pq)

    if idx > prev:
        prev = idx
    else:
        answer += 1
        heapq.heappush(pq, (num, accIdx))
        accIdx += 1


print(answer)
