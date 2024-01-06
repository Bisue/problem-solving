# 스킬트리
# https://school.programmers.co.kr/learn/courses/30/lessons/49993

from collections import deque

def solution(requirements, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        q = deque(requirements)
        
        possible = True
        for skill in tree:
            if skill in requirements:
                if q[0] == skill:
                    q.popleft()
                else:
                    possible = False
                    break
        
        if possible:
            answer += 1
    
    return answer
