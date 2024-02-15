# 도서관
# https://study.helloalgo.co.kr/study/1019/room/602/6595

import sys

N = int(sys.stdin.readline())

answer = None

rents = {}
for _ in range(N):
	name = sys.stdin.readline().rstrip()
	if name not in rents:
		rents[name] = 0
	rents[name] += 1
	if answer is None:
		answer = name
		continue
	
	if rents[name] > rents[answer]:
		answer = name
	elif rents[name] == rents[answer] and name < answer:
		answer = name

print(answer)
	
	