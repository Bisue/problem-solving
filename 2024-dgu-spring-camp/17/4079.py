# 증가하는 가장 긴 수열 찾기
# https://study.helloalgo.co.kr/study/1019/room/604/6610

N = int(input())
nums = list(map(int, input().split()))

# O(N^2)
def solution1():
	cnts = [1 for _ in range(N)]
	for i in range(1, N):
		for j in range(i):
			if nums[i] > nums[j]:
				cnts[i] = max(cnts[i], cnts[j] + 1)

	print(max(cnts))
	

# O(NlogN)
def solution2():
	cnts = [1 for _ in range(N)]
	mins = [1e10 for _ in range(N+1)]
	mins[0] = 0
	
	for i in range(N):
		idx = 0
		s, e = 0, N
		while s <= e:
			mid = (s+e)//2
			if mins[mid] < nums[i]:
				idx = mid
				s = mid+1
			else:
				e = mid-1
		
		mins[idx+1] = nums[i]
		cnts[i] = idx+1
		
	print(max(cnts))

solution2()
