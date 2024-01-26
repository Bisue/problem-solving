# 체스판 색칠놀이
# https://study.helloalgo.co.kr/study/1019/room/590/9364

N, M = map(int, input().split())
board = []
for _ in range(N):
	board.append(input())

def countDiffs(x, y):
	diffs = [0, 0]
	for i in range(x, x+8):
		for j in range(y, y+8):
			if (i+j)%2 == 0 and board[i][j] != 'W':
				diffs[0] += 1
			elif (i+j)%2 == 1 and board[i][j] != 'B':
				diffs[0] += 1
			if (i+j)%2 == 0 and board[i][j] != 'B':
				diffs[1] += 1
			elif (i+j)%2 == 1 and board[i][j] != 'W':
				diffs[1] += 1
	return min(diffs)
	
answer = 1e9
for x in range(N-8+1):
	for y in range(M-8+1):
		diff = countDiffs(x, y)
		answer = min(answer, diff)
		
print(answer)
