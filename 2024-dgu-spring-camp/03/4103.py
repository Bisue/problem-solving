# 표지
# https://study.helloalgo.co.kr/study/1019/room/590/6447

N = int(input())
target = input()
signs = []
for _ in range(N):
	signs.append(input())

answer = 0
for sign in signs:
	found = False
	for start in range(len(sign)):
		if found: break
		for span in range(1, len(sign)):
			buffer = []
			for i in range(len(target)):
				curIdx = start + span*i
				if curIdx < len(sign):
					buffer.append(sign[curIdx])
					
			cur = ''.join(buffer)
			if cur == target:
				found = True
				break
				
	# print(sign, found)
	if found:
		answer += 1

print(answer)
