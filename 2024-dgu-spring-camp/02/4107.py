# 바닥 도배
# https://study.helloalgo.co.kr/study/1019/room/589/6441

# r, b 주어짐
# L, W 구해야함(가로세로(내림차순))

# 사각형 둘레 길이 = r
# 사각형 넓이 = r + b

# L + W = r//2 + 1
# L*W = r + b

# L = r//2 + 1 - W
# W(-W + 1 + r//2) = r + b
# 

R, B = map(int, input().split())

# O(R)
def solution1(R, B):
	# l: 1 ~ R//2 + 1 (가로(긴 길이를 가로로 가정))
	for l in range(1, R//2 + 2):
		w = R//2 + 1 - l + 1
		
		if l < w:
			continue
		
		if l*w == R + B:
			print(f'{l} {w}')
			return
	
	return

# O(1)
def solution2(R, B):
	pass

solution1(R, B)
