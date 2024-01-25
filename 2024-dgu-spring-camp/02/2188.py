# 콜라 배달
# https://study.helloalgo.co.kr/study/1019/room/589/6425/source/

N = int(input())

# 1. O(N)
def solution1():
	minimum = 1e10
	for five in range(N//5 + 1):
		three = (N - five*5)//3

		if five*5 + three*3 == N:
			minimum = min(minimum, five + three)

	if minimum == 1e10:
		print(-1)
	else:
		print(minimum)
	
solution1()
