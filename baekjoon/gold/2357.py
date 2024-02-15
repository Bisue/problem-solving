# 최솟값과 최댓값
# https://www.acmicpc.net/problem/2357

import sys

N, M = map(int, sys.stdin.readline().split())

leafSize = 1
while leafSize < N:
    leafSize *= 2

minMaxTree = [[1e9, -1e9] for _ in range(leafSize*2)]

def addMinMaxTree(pos, num):
    idx = pos + leafSize
    
    minMaxTree[idx][0] = num
    minMaxTree[idx][1] = num
    while idx > 1:
        parentIdx = idx // 2
        if minMaxTree[idx][0] < minMaxTree[parentIdx][0]:
            minMaxTree[parentIdx][0] = minMaxTree[idx][0]
        if minMaxTree[idx][1] > minMaxTree[parentIdx][1]:
            minMaxTree[parentIdx][1] = minMaxTree[idx][1]
        
        idx = parentIdx

def queryMinTree(start, end):
    left, right = leafSize + start, leafSize + end
    
    minResult = 1e9
    maxResult = -1e9
    while left <= right:
        if left%2 == 1:
            minResult = min(minResult, minMaxTree[left][0])
            maxResult = max(maxResult, minMaxTree[left][1])
            left += 1
        left //= 2
        
        if right%2 == 0:
            minResult = min(minResult, minMaxTree[right][0])
            maxResult = max(maxResult, minMaxTree[right][1])
            right -= 1
        right //= 2
        
    return minResult, maxResult

for i in range(N):
    num = int(sys.stdin.readline())
    addMinMaxTree(i, num)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    
    mini, maxi = queryMinTree(a-1, b-1)
    print(mini, maxi)
