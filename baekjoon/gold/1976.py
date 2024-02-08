# 여행 가자
# https://www.acmicpc.net/problem/1976

# 유섭's 추가문제(유니온 파인드)

"""
A, B, C, B, D로 여행을 갈 수 있는지 여부
-> 같은 도시 여러 번 방문도 가능하다?
-> 그럼 모든 여행 경로가 연결만 되어있으면 가능
-> BFS로 연결된 그래프에 id를 붙이고, 여행 경로의 모든 도시가 같은 id면 YES 아니면 NO
"""

from collections import deque
import sys

N = int(input())
M = int(input())

# bfs
def solution1(N, M):
    linked = []
    for s in range(N):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        linked.append(row)

    regionId = 0
    regions = [-1 for _ in range(N)]
    for v in range(N):
        if regions[v] < 0:
            q = deque()
            q.append(v)
            regions[v] = regionId
            while len(q) > 0:
                cv = q.popleft()

                for nv in range(N):
                    if linked[cv][nv] == 1 and regions[nv] < 0:
                        q.append(nv)
                        regions[nv] = regionId

            regionId += 1

    plan = list(map(int, input().split()))
    id = regions[plan[0]-1]
    for pv in plan:
        if regions[pv-1] != id:
            print('NO')
            return

    print('YES')
    return


# union find
def solution2(N, M):
    pass

solution1(N, M)
