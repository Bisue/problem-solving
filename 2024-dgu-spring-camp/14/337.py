# 체육대회
# https://study.helloalgo.co.kr/study/1019/room/601/6580

"""
B의 가장 만만한 애부터 A의 가능한 제일 약한 애로 이기기
이때, B와 A를 정렬한 뒤 이기면 aCur++, bCur++, 못이기면 aCur++ 하면 A의 aCur 이전 원소는 다시 볼 필요가 없음
(B의 남은 원소는 bCur 이전 원소보다 무조건 크거나 같으므로)
"""

import sys

N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))

B.sort()
A.sort()

answer = 0

aCur, bCur = 0, 0
while aCur < N:
	if A[aCur] > B[bCur]:
		bCur += 1
		aCur += 1
		answer += 1
	else:
		aCur += 1
		
print(answer)
		