# 구간 합 구하기
# https://www.acmicpc.net/problem/2042

# [TODO] 세그먼트 트리 구현 익히기/방법 최적화하기

import sys

"""
       15
   10      5
 3   7   5   0
1 2 3 4 5 0 0 0
"""

N, M, K = map(int, sys.stdin.readline().split())

leafSize = 1
while leafSize < N:
    leafSize *= 2
    
segmentTree = [0 for _ in range(2*leafSize)]
leafSize -= 1

def update(idx, num):
    idx += leafSize # to leafIdx
    
    original = segmentTree[idx]
    diff = num - original
    
    parentIdx = idx//2
    while idx != parentIdx:
        segmentTree[idx] += diff
        
        idx = parentIdx
        parentIdx = idx//2
    
def query(start, end):
    result = 0
    
    start = leafSize + start
    end = leafSize + end
    
    turn = True
    while start <= end:
        # print(turn, result, (start, end))
        if turn:
            if start%2 == 1:
                result += segmentTree[start]
                start += 1
            start //= 2
        else:
            if end%2 == 0:
                result += segmentTree[end]
                end -= 1
            end //= 2
        turn = not turn
        
    # print(turn, result, (start, end))
                
    return result

for i in range(1, N+1):
    num = int(sys.stdin.readline())
    update(i, num)
    
# print(list(zip(range(2*(leafSize + 1)), segmentTree)))
    
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == 1:
        # change b to c
        update(b, c)
    elif a == 2:
        # change sum b ~ c
        print(query(b, c))
        
    # print('seg: ', list(zip(range(2*(leafSize + 1)), segmentTree)))
