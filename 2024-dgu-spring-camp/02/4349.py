# 올바른 삼각형
# https://study.helloalgo.co.kr/study/1019/room/589/6439

# 올바른 삼각형?
# => 3점 중, pivot 잡고 pivot.x, pivot.y 각각 같은 점 하나씩

N = int(input())
points = []
for _ in range(N):
	x, y = map(int, input().split())
	points.append((x, y))
	
def calcDoubledArea(p1, p2, p3):
	# pivot: p1
	if p1[0] == p2[0] and p1[1] == p3[1]:
		return abs(p1[0] - p3[0])*abs(p1[1] - p2[1])
	elif p1[0] == p3[0] and p1[1] == p2[1]:
		return abs(p1[0] - p2[0])*abs(p1[1] - p3[1])
	# pivot: p2
	elif p2[0] == p1[0] and p2[1] == p3[1]:
		return abs(p2[0] - p3[0])*abs(p2[1] - p1[1])
	elif p2[0] == p3[0] and p2[1] == p1[1]:
		return abs(p2[0] - p1[0])*abs(p2[1] - p3[1])
	# pivot: p3
	elif p3[0] == p1[0] and p3[1] == p2[1]:
		return abs(p3[0] - p2[0])*abs(p3[1] - p1[1])
	elif p3[0] == p2[0] and p3[1] == p1[1]:
		return abs(p3[0] - p1[0])*abs(p3[1] - p2[1])
	
	return -1

maxArea = 0
for i in range(N):
	for j in range(i+1, N):
		for k in range(j+1, N):
			doubledArea = calcDoubledArea(points[i], points[j], points[k])
			
			if doubledArea > 0:
				maxArea = max(maxArea, doubledArea)
			
			# print(points[i], points[j], points[k])
			
print(maxArea)
