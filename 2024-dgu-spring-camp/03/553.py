# 화살표그리기(KOI전국2018_초등부_2)
# https://study.helloalgo.co.kr/study/1019/room/590/6443

# O(n^2)
def solution1():
	N = int(input())
	
	points = [[] for _ in range(N + 1)]
	for _ in range(N):
		x, color = map(int, input().split())
		points[color].append(x)
	
	def getLocalMinimum(x, points):
		result = 1e9
		f, b = x+1, x-1
		# print(points, f, x, b)
		if f < len(points):
			result = min(result, points[f] - points[x])
			# print('f', points[f] - points[x])
		if b >= 0:
			result = min(result, points[x] - points[b])
			# print('b', points[x] - points[b])
		
		# print(points, result)
		return result
	
	answer = 0
	for i in range(N):
		points[i].sort()
		for j in range(len(points[i])):
			answer += getLocalMinimum(j, points[i])
	
	print(answer)
		
	
# O(N) or O(NlogN)
def solution2():
	N = int(input())
	
	points = []
	for _ in range(N):
		x, color = map(int, input().split())
		points.append((color, x))
		
	points.sort(key=lambda p: (p[0], p[1]))
	
	def getLocalMinimum(x, points):
		result = 1e9
		f, b = x+1, x-1
		# print(points, f, x, b)
		if f < len(points) and points[x][0] == points[f][0]:
			result = min(result, points[f][1] - points[x][1])
			# print('f', points[f] - points[x])
		if b >= 0 and points[x][0] == points[b][0]:
			result = min(result, points[x][1] - points[b][1])
			# print('b', points[x] - points[b])
		
		# print(points, result)
		return result
	
	answer = 0
	for i in range(N):
		cur = getLocalMinimum(i, points)
		answer += cur
		
	print(answer)

# solution1()
solution2()
