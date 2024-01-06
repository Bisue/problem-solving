# 가장 먼 노드
# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    dists = [-1 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    q = deque()
    q.append(1)
    dists[1] = 0
    while len(q) > 0:
        cv = q.popleft()
        
        for nv in graph[cv]:
            if dists[nv] == -1:
                q.append(nv)
                dists[nv] = dists[cv] + 1
    
    return dists.count(max(dists))
