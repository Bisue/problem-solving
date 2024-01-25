# 3장으로 하는 블랙잭
# https://study.helloalgo.co.kr/study/1019/room/589/6437

N, M = map(int, input().split())
cards = list(map(int, input().split()))

# O(N^3)
def solution1():
	maxSum = 0
	for i in range(N):
		for j in range(i+1, N):
			for k in range(j+1, N):
				now = cards[i] + cards[j] + cards[k]
				if now > M:
					continue

				maxSum = max(maxSum, now)

	print(maxSum)

# O(?)
def solution2():
	pass

solution1()
