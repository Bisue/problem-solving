# 삼각 달팽이
# https://school.programmers.co.kr/learn/courses/30/lessons/68645

dirs = [
    (1, 0),
    (0, 1),
    (-1, -1),
]

def solution(n):
    triangle = [[0 for _ in range(h+1)] for h in range(n)]
    
    def isValid(x, y):
        return 0 <= x < n and 0 <= y < len(triangle[x])
    
    cx, cy, cd = 0, 0, 0
    now = 1
    for length in range(n, 0, -1):
        for i in range(length):
            triangle[cx][cy] = now
            now += 1
            
            if i == length - 1:
                cd = (cd + 1) % 3
            dx, dy = dirs[cd]
            cx, cy = cx + dx, cy + dy

    answer = []
    for row in triangle:
        for num in row:
            answer.append(num)
        
    return answer
