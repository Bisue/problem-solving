# DFS와 BFS
# https://study.helloalgo.co.kr/study/1019/room/596/6537

from collections import deque

N, M, V = map(int, input().split())

graph = { i: [] for i in range(1, N+1) }
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
for s in graph:
    graph[s].sort()

dfsVisited = set()
def printDfs(cur):
    dfsVisited.add(cur)
    print(cur, end=' ')
    
    for nv in graph[cur]:
        if nv not in dfsVisited:
            printDfs(nv)
            
def printBfs(start):
    q = deque()
    bfsVisited = set()
    
    q.append(start)
    bfsVisited.add(start)
    while len(q) > 0:
        cur = q.popleft()
        print(cur, end=' ')
        
        for nv in graph[cur]:
            if nv not in bfsVisited:
                q.append(nv)
                bfsVisited.add(nv)

dfsVisited.add(V)
printDfs(V)
print()
printBfs(V)
print()
