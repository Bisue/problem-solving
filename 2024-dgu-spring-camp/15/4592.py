# 마라톤
# https://study.helloalgo.co.kr/study/1019/room/602/6596

"""
동명 이인이 있을 수 있으므로,
set이 아닌 카운팅을 해야함
"""

import sys

N = int(input())

losers = {}
for _ in range(N):
	name = sys.stdin.readline().rstrip()
	if name not in losers:
		losers[name] = 0
	losers[name] += 1

for _ in range(N-1):
	name = sys.stdin.readline().rstrip()
	if name in losers:
		losers[name] -= 1
		if losers[name] == 0:
			del losers[name]

print(list(losers.keys())[0]) # 무조건 1명이므로
	