# 일곱 난쟁이
# https://study.helloalgo.co.kr/study/1019/room/589/6438

heights = []
for _ in range(9):
	heights.append(int(input()))
	
heights.sort()

target = sum(heights) - 100

imposters = set()
for i in range(len(heights)):
	for j in range(i + 1, len(heights)):
		if heights[i] + heights[j] == target:
			imposters.add(i)
			imposters.add(j)

for i in range(len(heights)):
	if i in imposters:
		continue
		
	print(heights[i])
