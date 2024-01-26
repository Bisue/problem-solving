# 고기잡이(L)
# https://study.helloalgo.co.kr/study/1019/room/590/6450

N, M = map(int, input().split())
H, W = map(int, input().split())
board = []
for _ in range(N):
	board.append(list(map(int, input().split())))
	
maxVal = 0
for x in range(N-H+1):
	for y in range(M-W+1):
		cur = 0
		for i in range(x, x+H):
			for j in range(y, y+W):
				cur += board[i][j]
		maxVal = max(maxVal, cur)
  
print(maxVal)
