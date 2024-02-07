# Counting Haybles(USACO_2016_DEC_SILVER_1)
# https://study.helloalgo.co.kr/study/1019/room/598/6554

import sys

# query: A B 일때, (B 초과인 최대 인덱스) - (A 이상인 최소 인덱스)

N, Q = map(int, input().split())
objects = list(map(int, input().split()))
objects.sort()

def findStartIdx(minimum):
	start, end = 0, N-1
	answer = N
	while start <= end:
		mid = (start + end)//2
		
		if objects[mid] >= minimum:
			answer = mid
			end = mid-1
		else:
			start = mid+1
		
	return answer

def findEndIdx(maximum):
	start, end = 0, N-1
	answer = N
	while start <= end:
		mid = (start + end)//2
		
		if objects[mid] > maximum:
			answer = mid
			end = mid-1
		else:
			start = mid+1
		
	return answer
	

for _ in range(Q):
	a, b = map(int, sys.stdin.readline().rstrip().split())
	
	minIdx = findStartIdx(a)
	maxIdx = findEndIdx(b)
	print(maxIdx - minIdx)
	