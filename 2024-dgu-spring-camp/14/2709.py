# 배치하기
# https://study.helloalgo.co.kr/study/1019/room/601/6577

# 왠지 A가 오름차순, B가 내림차순이면
# X = 작은 값 x 큰 값 + ... 이라 최소일 것 같다. 
# [TODO] 증명?

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

X = 0
for i in range(N):
	X += A[i]*B[i]
	
print(X)
