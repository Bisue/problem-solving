# 정사각형 찾기
# https://study.helloalgo.co.kr/study/1019/room/590/9365

N, M = map(int, input().split())
board = []
for _ in range(N):
	board.append(list(map(int, list(input()))))
	
def solution1(N, M, board):
	for size in range(min(N, M), 0, -1): # min(N,M) -> 1
		for x in range(N-size+1):
			for y in range(M-size+1):
				target = board[x][y]
				if board[x][y] == board[x+size-1][y] and board[x][y] == board[x][y+size-1] and board[x][y] == board[x+size-1][y+size-1]:
					return size*size
				
	return 0

print(solution1(N, M, board))
