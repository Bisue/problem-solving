# 듣보잡
# https://study.helloalgo.co.kr/study/1019/room/602/6592

import sys

N, M = map(int, sys.stdin.readline().split())

notHear = set()
for _ in range(N):
	name = sys.stdin.readline().rstrip()
	notHear.add(name)
	
notSee = set()
for _ in range(M):
	name = sys.stdin.readline().rstrip()
	notSee.add(name)
	
print(len(notHear.intersection(notSee)))
	