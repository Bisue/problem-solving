# 소가 길을 건너간 이유 2(USACO_2017_FEB_BRONZE_2)(중간고사)
# https://study.helloalgo.co.kr/exam/616/solve/3988

# (처음에 스택으로 접근했다가 실패 - ABCBCADEDE... 에서 반례 생김)
# (-> 그냥 주어진 문자열 O(N^2)으로 순회하면서 특정 알파벳 구간 내)
# (   홀수인 알파벳이 있으면 걔랑 겹치는 쌍.)

cows = input()

checked = set()
pairs = set()
for i in range(len(cows)):
	if cows[i] in checked:
		continue
	
	targets = set()
	checked.add(cows[i])
	for j in range(i+1, len(cows)):
		if cows[i] == cows[j]:
			break
			
		if cows[j] in targets:
			targets.remove(cows[j])
		else:
			targets.add(cows[j])
	
	for t in targets:
		c1, c2 = cows[i], t
		if c1 > c2:
			c1, c2 = c2, c1
		pairs.add((c1, c2))
		
# print(pairs)
print(len(pairs))
