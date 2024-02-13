# 수 정렬하기
# https://study.helloalgo.co.kr/study/1019/room/600/6576/source/829006/

# Array 트리 연습용 min-heap 직접 구현.
# - heap-sort

import sys

"""
        0
   1          2
 3   4     5     6
7 8 9 10 11 12 13 14

left: cur*2 + 1
right: cur*2 + 2
parent: cur//2 -1 if cur%2 == 0 else cur//2
"""

heap = []

def getLeftIdx(cur):
    return cur*2 + 1
def getRightIdx(cur):
    return cur*2 + 2
def getParentIdx(cur):
    return cur//2 - 1 if cur%2 == 0 else cur//2

def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

def heapUp(idx):
    pIdx = getParentIdx(idx)
    while pIdx >= 0:
        if heap[idx] < heap[pIdx]:
            swap(heap, idx, pIdx)
        
        idx = pIdx
        pIdx = getParentIdx(idx)
        
def heapDown(idx):
    while True:
        left, right = getLeftIdx(idx), getRightIdx(idx)
        if left < len(heap) and heap[left] < heap[idx] and (right >= len(heap) or heap[left] <= heap[right]):
            swap(heap, idx, left)
            idx = left
        elif right < len(heap) and heap[right] < heap[idx] and heap[right] <= heap[left]:
            swap(heap, idx, right)
            idx = right
        else:
            break

def add(num):
    heap.append(num)
    heapUp(len(heap)-1)
    
def remove():
    if len(heap) == 0:
        return heap.pop()
    
    result = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    heapDown(0)
    
    return result

N = int(sys.stdin.readline())
for _ in range(N):
    x = int(sys.stdin.readline())
    add(x)

answers = []
while len(heap) > 0:
    answers.append(str(remove()))
    
print('\n'.join(answers))
