# lower bound
# https://study.helloalgo.co.kr/study/1019/room/598/6551

N = int(input())
nums = list(map(int, input().split()))
K = int(input())

# 범위(start~end)를 탐색할 범위로 정의하고,
# 답일 가능성이 있을 때 answer 변수로 위치를 대입한 뒤
# 범위는 무조건 mid-1, mid+1로 줄임.
# while 조건은 start <= end(탐색할 범위가 1 이상일 때까지)

def lowerBound(n, arr, k):
	start, end = 0, n-1
	answer = None
	while start <= end:
		mid = (start + end)//2

		if nums[mid] >= k:
			answer = mid
			end = mid-1
		else:
			start = mid+1
			
	return answer

result = lowerBound(N, nums, K)
if result is None:
	print(N+1)
else:
	print(result+1)
