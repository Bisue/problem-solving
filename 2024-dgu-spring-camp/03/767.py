# 덩치(KOI지역2013_초등부_2)
# https://study.helloalgo.co.kr/study/1019/room/590/6442

# x1 > x2 and y1 > y2 면 (x1, y1)이 더 큰 덩치

N = int(input())

inbodies = []
for _ in range(N):
	w, h = map(int, input().split())
	inbodies.append((w, h))
	
inbodies.sort(key=lambda wh: wh[0], reverse=True)

print(inbodies)

orders = [0 for _ in range(N)]
for i in range(N):
	order = 1
	for j in range(N):
		if i == j:
			continue
		if inbodies[i][0] < inbodies[j][0] and inbodies[i][1] < inbodies[j][1]:
			order += 1
	orders[i] = order

print(' '.join(map(str, orders)))
