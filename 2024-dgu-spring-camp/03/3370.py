# 마라톤1
# https://study.helloalgo.co.kr/study/1019/room/590/6448

N = int(input())
points = []
for _ in range(N):
	x, y = map(int, input().split())
	points.append((x, y))
	
def calcDist(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
	
total = 0
# 안빠지고 달렸을 때 전체 거리
for i in range(N-1):
	dist = calcDist(points[i+1], points[i])
	total += dist

answer = total
# i번째 체크포인트를 스킵할 때
for i in range(1, N-1):
	# i-1 <-> i, i <-> i+1 거리는 빼고
	minus = calcDist(points[i-1], points[i]) + calcDist(points[i+1], points[i])
	# i-1 <-> i+1 거리는 더함
	plus = calcDist(points[i-1], points[i+1])
	
	# i번째 체크포인트를 빠졌을 때 총 거리: total - minus + plus
	answer = min(answer, total - minus + plus)
	
print(answer)
	