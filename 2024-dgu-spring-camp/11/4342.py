# 공유기 설치
# https://study.helloalgo.co.kr/study/1019/room/598/6558

# 가장 인접한 공유기 사이 거리가 k 이상일 때, 모두 설치가 가능한가?
# -> 모든 공유기 사이 거리가 k 이상일 때, 모두 설치가 가능한가?

N, C = map(int, input().split())
houses = list(map(int, input().split()))
houses.sort()

def isPossible(houses, dist, k):
	installed = 1
	prev = houses[0]
	for i in range(1, N):
		if houses[i] - prev >= mid:
			installed += 1
			prev = houses[i]
			
	return installed >= k

start, end = 1, 1_000_000_000
answer = -1
while start <= end:
	mid = (start + end)//2
	
	# 가능?
	if isPossible(houses, mid, C):
		answer = mid
		start = mid + 1
	else:
		end = mid - 1
		
print(answer)
