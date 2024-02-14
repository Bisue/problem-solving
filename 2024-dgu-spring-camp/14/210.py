# 회의실 배정
# https://study.helloalgo.co.kr/study/1019/room/601/6588

"""
첫번째로 끝나는 시간을 오름차순으로 정렬하고,
(두번째로 시작하는 시간을 내림차순 정렬하면)
(이건 안해도 되나?)

회의실 시간표의 앞단부터 채워나갈 수 있다
"""

import sys

N = int(input())
conferences = []
for _ in range(N):
	s, e = map(int, sys.stdin.readline().split())
	conferences.append((s, e))
	
conferences.sort(key=lambda c: c[1])

answer = 0
prevE = 0
for s, e in conferences:
	if s >= prevE:
		answer += 1
		prevE = e
	
print(answer)
