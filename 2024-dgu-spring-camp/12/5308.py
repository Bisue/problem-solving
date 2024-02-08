# Hello Algo
# https://study.helloalgo.co.kr/study/1019/room/599/6568

# Welcome(i)의 x번째 문자(x는 0부터 센다고 가정)
# => x < len(Welcome(i-1)) 이면 Welcome(i-1)의 x번째 문자열
# => len(Welcome(i-1)) <= x < len(Welcome(i-1)) + len(Welcome(i-2)) 이면 Welcome(i-2)의 x-len(Welcome(i-1))번째 문자열

import sys

welcomeLengthes = [6, 11]
while welcomeLengthes[-1] < 2**30 - 1:
	nextLength = welcomeLengthes[-1] + welcomeLengthes[-2]
	welcomeLengthes.append(nextLength)

def getWelcomeChar(i, x):
	global welcomeLengthes
	
	if i == 0:
		return 'Hello '[x]
	elif i == 1:
		return 'Hello Algo '[x]
	
	if x < welcomeLengthes[i-1]:
		return getWelcomeChar(i-1, x)
	elif x < welcomeLengthes[i-1] + welcomeLengthes[i-2]:
		return getWelcomeChar(i-2, x-welcomeLengthes[i-1])

T = int(input())
for _ in range(T):
	x = int(sys.stdin.readline())-1
	ch = getWelcomeChar(len(welcomeLengthes), x)
	if ch == ' ':
		print('Hello Algo')
	else:
		print(ch)
