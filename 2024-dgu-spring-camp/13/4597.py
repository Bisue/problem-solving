# 최소 힙
# https://study.helloalgo.co.kr/study/1019/room/600/6569

# Array 트리 연습용 min-heap 직접 구현.

import sys

heap = [None]
"""
   1 
 2   3
4 5 6 7

left: cur*2
right: cur*2 + 1
parent: cur//2
"""

def heapify(idx):
	parentIdx = idx//2
	while parentIdx > 0:
		if heap[parentIdx] > heap[idx]:
			heap[parentIdx], heap[idx] = heap[idx], heap[parentIdx]
		
		idx = parentIdx
		parentIdx = idx//2

def addElement(el):
	heap.append(el)
	
	heapify(len(heap)-1)

def removeElement():
	result = heap[1]
	
	if len(heap) == 2:
		return heap.pop()
	
	heap[1] = heap.pop()
	
	idx = 1
	while True:
		left, right = idx*2, idx*2 + 1
		# print(heap, idx, left, right)
			
		if left < len(heap) and heap[left] < heap[idx] and (right >= len(heap) or heap[left] <= heap[right]):
			heap[idx], heap[left] = heap[left], heap[idx]
			idx = left
		elif right < len(heap) and heap[right] < heap[idx] and heap[right] <= heap[left]:
			heap[idx], heap[right] = heap[right], heap[idx]
			idx = right
		else:
			break
			
	return result

N = int(input())
for _ in range(N):
	x = int(sys.stdin.readline())
	
	if x == 0:
		if len(heap) == 1:
			print(0)
		else:
			print(removeElement())
	else:
		addElement(x)
	
	