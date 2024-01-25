# 삼각화단 만들기(S)
# https://study.helloalgo.co.kr/study/1019/room/589/6440

N = int(input())

def solution1():
	# [TIP] 그냥 O(1)로 대체가능(k < i + j, (i <= j <= k 이므로))
	def checkPossible(lengthes):
		biggest = 0

		for i in range(len(lengthes)):
			if lengthes[i] >= lengthes[biggest]:
				biggest = i

		remained = 0
		for i in range(len(lengthes)):
			if i == biggest:
				continue

			remained += lengthes[i]

		return lengthes[biggest] < remained

	answer = 0
	for i in range(1, N):
		for j in range(i, N):
			k = N - i - j
			if k <= 0 or k < j:
				continue

			if checkPossible([i, j, k]):
				answer += 1
	print(answer)

# O(N)
def solution2():
	answer = 0
	for i in range(1, N):
		remained = N - i
		halfRamained = remained//2
		if remained%2 == 0:
			j, k = halfRamained, halfRamained
		else:
			j, k = halfRamained, halfRamained + 1
		
		if not i <= j <= k or i + j <= k:
			continue
			
		print(i, j, k)

		answer += 1
		
	print(answer)

# [TODO][TIP] j와 k의 관계 이용
# 1 n-i-1
# 2 n-i-2 ...
# ~ (n-i)//2 까지 (why? j <= k)

# 이때 i <= j <= k 이므로, sum += max((n-i)//2 - (i-1), 0)

solution1()
