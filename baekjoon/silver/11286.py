# 절댓값 힙
# https://www.acmicpc.net/problem/11286

import sys
import heapq as hq

N = int(input())

pq = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(pq) == 0:
            print(0)
            continue
        ab, val = hq.heappop(pq)
        print(val)
    else:
        hq.heappush(pq, (abs(x), x))
        

