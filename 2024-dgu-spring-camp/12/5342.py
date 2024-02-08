# 하노이의 탑
# https://study.helloalgo.co.kr/study/1019/room/599/6567

# 1번, 2번, 3번 장대에서
# 1~N개를 1번에서 3번으로 옮기려면
# - 1~N-1개를 1번에서 2번으로 옮기고
# - N번 원반을 1번에서 3번으로 옮긴 뒤
# - 1~N-1개를 2번에서 3번으로 옮기면 된다
#   - 1~N-1개를 2번에서 3번으로 옮기려면
#     - 1~N-2개를 2번에서 1번으로 옮기고
#     - N-1번 원반을 2번에서 3번으로 옮긴 뒤
#     - 1~N-2개를 1번에서 3번으로 옮기면 된다
# ...

# -> N개를 x에서 y로 옮기려면
#   - N-1개를 x에서 6-x-y(다른 기둥)으로 옮기고
#   - N번 원반을 x에서 y로 옮긴 뒤
#   - N-1개를 6-x-y(다른 기둥)에서 y로 옮기면 된다

N = int(input())

answer = 0
logs = []
def hanoi(n, x, y):
	global answer
	
	if n==1:
		logs.append((x, y))
		answer += 1
		return
	
	hanoi(n-1, x, 6-x-y)
	hanoi(1, x, y)
	hanoi(n-1, 6-x-y, y)

hanoi(N, 1, 3)

print(answer)
for a, b in logs:
	print(f'{a} {b}')
