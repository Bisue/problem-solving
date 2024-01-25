# 방 배정하기(KOI전국2017_초등부_2_중등부_1)
# https://study.helloalgo.co.kr/study/1019/room/589/6426/source/

A, B, C, N = map(int, input().split())

def solution():
	for i in range(N//A + 1):
		for j in range(N//B + 1):
			for k in range(N//C + 1):
				if i*A + j*B + k*C == N:
					return '1'

	return '0'

print(solution())
