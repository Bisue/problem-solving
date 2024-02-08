# 과정 출력하기(버블)
# https://study.helloalgo.co.kr/study/1019/room/599/6563

N = int(input())
nums = list(map(int, input().split()))

print(' '.join(map(str, nums)))
for i in range(N):
	pos = i
	for j in range(N-i-1):
		# print(i, (j, j+1), nums[j], nums[j+1])
		if nums[pos] > nums[j+1]:
			nums[pos], nums[j+1] = nums[j+1], nums[pos]
			poos
			print(' '.join(map(str, nums)))
