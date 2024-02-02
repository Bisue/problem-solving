# 수강신청(중간고사)
# https://study.helloalgo.co.kr/exam/616/solve/3989

ids = list(map(int, input().split()))
N = int(input())

success = []
for _ in range(N):
	a, b = map(int, input().split())
	success.append({ a, b })

answer = 0
for i in range(N):
	for j in range(i+1, N):
		cur = success[i] | success[j]
		
		found = True
		for k in ids:
			if k not in cur:
				found = False
				
		if found:
			answer += 1

print(answer)
