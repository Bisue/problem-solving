# 점심식사(COCI_2016_CONTEST6_2)
# https://study.helloalgo.co.kr/study/1019/room/589/6434

N, C = map(int, input().split())
foods = list(map(int, input().split()))

maxKind = 0
for i in range(N):
	curWeights, curKind = 0, 0
	for j in range(i, N):
		nextWeights = curWeights + foods[j]
		if nextWeights > C:
			continue
		else:
			curWeights = nextWeights
			curKind += 1
	
	maxKind = max(maxKind, curKind)
	
print(maxKind)
