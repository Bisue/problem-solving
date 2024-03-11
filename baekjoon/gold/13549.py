# 숨바꼭질 3
# https://www.acmicpc.net/problem/13549

import heapq as hq

N, K = map(int, input().split())


def getMinTime(N, K):
    pq = []
    times = [1e10 for _ in range(200_001)]

    hq.heappush(pq, (0, N))
    times[N] = 0
    while len(pq) > 0:
        cd, cp = hq.heappop(pq)
        if cd > times[cp]:
            continue
        if cp == K:
            break

        for n in [cp - 1, cp + 1, cp * 2]:
            if n < 0 or n > 200_000:
                continue

            if n == cp * 2:
                nd = cd
            else:
                nd = cd + 1

            if nd < times[n]:
                hq.heappush(pq, (nd, n))
                times[n] = nd

    return times[K]


if N >= K:
    print(N - K)
else:
    print(getMinTime(N, K))
