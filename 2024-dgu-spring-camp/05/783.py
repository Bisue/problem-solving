# 싸이클(KOI지역2012_초등부_2)
# https://study.helloalgo.co.kr/study/1019/room/592/6467

N, P = map(int, input().split())

orders = [-1 for _ in range(P)]
answer = -1
def dfs(n, p, num, cnt):
	global orders, answer
	
	if answer >= 0:
		return
	
	if orders[num] >= 0:
		# print(num, cnt, orders[nextNum], orders)
		answer = cnt - orders[num]
		return
	
	# print(num, cnt)
	orders[num] = cnt
	
	dfs(n, p, (num*n)%p, cnt + 1)

dfs(N, P, N*N%P, 0)
print(answer)
