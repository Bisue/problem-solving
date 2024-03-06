# 케이크 자르기
# https://www.acmicpc.net/problem/17179

"""
문제 오류?
- 문제대로라면 정확히 query 번만 잘랐을 때의 최댓값을 구해야 하는데,
코드에서 cuts == query 일때만 answer를 갱신하면 틀린 걸로 나오고,
코드에서 cuts > query 일때도 answer를 갱신해야 맞은 걸로 뜸.

알아보기
"""

import sys

N, M, L = map(int, sys.stdin.readline().split())
lines = []
for _ in range(M):
    lines.append(int(sys.stdin.readline()))
    
lines.sort()

for _ in range(N):
    query = int(sys.stdin.readline())
    
    answer = 0
    s, e = 1, L
    while s <= e:
        m = (s + e)//2
        # print((s, m, e))
        
        cuts = 0
        prev = 0
        for line in lines:
            if line - prev >= m:
                # print(' ||', line)
                cuts += 1
                prev = line
        if L - prev >= m:
            # print(' ||', L)
            cuts += 1
            prev = L
            
        # 조각 수는 cuts 개 이지만, 자르는 수(query)는 cuts - 1
        cuts = cuts - 1
        # print(' -', cuts)
            
        if cuts == query:
            answer = m
            s = m + 1
        elif cuts > query:
            answer = m
            s = m + 1
        else:
            e = m - 1
            
    print(answer)
        
        
