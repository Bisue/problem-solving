# 리코쳇 로봇
# https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

dirs = [
    (-1, 0),
    (0, -1),
    (1, 0),
    (0, 1),
]

def solution(board):
    def isValid(x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[x])
    
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 'R':
                sx, sy = x, y
    
    q = deque()
    visited = set()
    q.append((sx, sy, 0))
    visited.add((sx, sy))
    while len(q) > 0:
        cx, cy, cd = q.popleft()
        
        if board[cx][cy] == 'G':
            return cd
        
        for dx, dy in dirs:
            nx, ny = cx, cy
            while isValid(nx, ny) and board[nx][ny] != 'D':
                nx, ny = nx+dx, ny+dy
            nx, ny = nx-dx, ny-dy

            if isValid(nx, ny) and board[nx][ny] != 'D' and (nx, ny) not in visited:
                q.append((nx, ny, cd+1))
                visited.add((nx, ny))
    
    return -1
