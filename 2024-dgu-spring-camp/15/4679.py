# 출퇴근
# https://study.helloalgo.co.kr/study/1019/room/602/6593

import sys

N = int(sys.stdin.readline())
inside = set()

for _ in range(N):
	name, tag = sys.stdin.readline().split()
	if tag == 'enter':
		inside.add(name)
	else:
		inside.remove(name)
		
print(len(inside))
for name in sorted(inside):
	print(name)
