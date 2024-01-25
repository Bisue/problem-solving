# Milk Pails(USACO_2016_FEB_BRONZ_1)
# https://study.helloalgo.co.kr/study/1019/room/589/6435

X, Y, M = map(int, input().split())

maxV = 0
for i in range(M//X + 1):
	j = (M - X*i)//Y
	
	maxV = max(maxV, X*i + Y*j)
	
print(maxV)
