# 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

dirs = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

def solution(maps):
    visited = set()
    
    def isValid(x, y):
        return 0 <= x < len(maps) and 0 <= y < len(maps[x])
    
    def explore(sx, sy):
        food = 0
        
        q = deque()
        q.append((sx, sy))
        visited.add((sx, sy))
        while len(q) > 0:
            cx, cy = q.popleft()
            
            food += int(maps[cx][cy])
            
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                
                if isValid(nx, ny) and maps[nx][ny] != 'X' and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
                    
        return food
    
    islands = []
    for x in range(len(maps)):
        for y in range(len(maps[x])):
            if maps[x][y] != 'X' and (x, y) not in visited:
                islands.append(explore(x, y))
    
    if len(islands) > 0:
        return sorted(islands)
    else:
        return [-1]
