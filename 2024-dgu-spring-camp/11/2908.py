# upper bound
# https://study.helloalgo.co.kr/study/1019/room/598/6552

N = int(input())
nums = list(map(int, input().split()))
K = int(input())

def upperBound(n, arr, k):
	start, end = 0, n-1
	answer = None
	while start <= end:
		mid = (start + end)//2
		
		if nums[mid] > k:
			answer = mid
			end = mid-1
		else:
			start = mid+1
			
	return answer

result = upperBound(N, nums, K)
if result is None:
	print(N+1)
else:
	print(result+1)
