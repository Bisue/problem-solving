# 등산 코스 정하기(2022 KAKAO TECH INTERNSHIP)
# https://school.programmers.co.kr/learn/courses/30/lessons/118669

import heapq as hq

def solution(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)

    routes = { i: [] for i in range(1, n+1) }
    for s, e, w in paths:
        routes[s].append((w, e))
        routes[e].append((w, s))

    def findRouteAll():
        pq = []
        dists = [1e10 for _ in range(n+1)]
        visited = set()
        for gate in gates:
            hq.heappush(pq, (0, gate))
            dists[gate] = 0

        minIntensity = 1e10
        answer = [1e10, 1e10]
        while len(pq) > 0:
            cw, cn = hq.heappop(pq)
            visited.add(cn)

            if cn in summits:
                if cw < minIntensity or (cw == minIntensity and cn < answer[0]):
                    minIntensity = cw
                    answer = [cn, cw]

                continue
            if cw > answer[1]:
                continue

            for nw, nn in routes[cn]:
                ni = max(cw, nw)
                if nn not in visited and dists[nn] > ni and nn not in gates:
                    hq.heappush(pq, (ni, nn))
                    dists[nn] = ni

        return answer

    return findRouteAll()
