# N-QUEEN
# https://study.helloalgo.co.kr/study/1019/room/591/9379/submit-status/

N = int(input())

diffAvoid = {}
sumAvoid = {}
yAvoid = {}
def fill(x, y, undo=False):
	diff, suma = x-y, x+y
	if diff not in diffAvoid:
		diffAvoid[diff] = 0
	if suma not in sumAvoid:
		sumAvoid[suma] = 0
	if y not in yAvoid:
		yAvoid[y] = 0
	
	amount = 1
	if undo:
		amount = -1
	diffAvoid[diff] += amount
	sumAvoid[suma] += amount
	yAvoid[y] += amount
	
	if diffAvoid[diff] == 0:
		del diffAvoid[diff]
	if sumAvoid[suma] == 0:
		del sumAvoid[suma]
	if yAvoid[y] == 0:
		del yAvoid[y]
	
	return

answer = 0
def dfs(x):
	global answer, tries
	
	if x == N:
		answer += 1
		return
	
	for i in range(N):
		if x-i not in diffAvoid and x+i not in sumAvoid and i not in yAvoid:
			fill(x, i) # O(1)
			dfs(x + 1)
			fill(x, i, undo=True) # O(1)

dfs(0)
print(answer)
