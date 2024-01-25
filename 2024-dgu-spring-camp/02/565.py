# 올림픽(KOI전국2013_초등부_1)
# https://study.helloalgo.co.kr/study/1019/room/589/6453

# sort: g - s - b

N, K = map(int, input().split())
medals = []
for _ in range(N):
	id, gold, silver, bronze = map(int, input().split())
	medals.append((gold, silver, bronze, id))

medals.sort(key=lambda m: (m[0], m[1], m[2]), reverse=True)

orderDict = {}
prev = (-1, -1, -1)
order = 0
for g, s, b, i in medals:
	pg, ps, pb = prev
	if g != pg or s != ps or b != pb:
		prev = (g, s, b)
		order += 1
		
	orderDict[i] = order

print(orderDict[K])
