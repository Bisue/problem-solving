# 숫자 야구
# https://study.helloalgo.co.kr/study/1019/room/589/6436/source/

N = int(input())
turns = []
for _ in range(N):
	tokens = input().split()
	predict, strikes, balls = list(map(int, list(tokens[0]))), int(tokens[1]), int(tokens[2])
	turns.append((predict, strikes, balls))

# O(1) (111~999 (중복 숫자 제외))
def solution1(N, turns):
	answer = 0
	# [TODO] for 범위 최적화
	for target in range(111, 1000):
		targetTokens = [target//100, (target%100)//10, target%10]
		if targetTokens[0] == targetTokens[1] or targetTokens[0] == targetTokens[2] or targetTokens[1] == targetTokens[2]:
			continue
		if 0 in targetTokens:
			continue
		
		possible = True
		for p, s, b in turns: # O(N)
			cs, cb = 0, 0
			for i in range(len(p)): # O(1) (3)
				if p[i] == targetTokens[i]:
					cs += 1
				elif p[i] in targetTokens: # in: O(1) (3)
					cb += 1
			if cs != s or cb != b:
				possible = False
				break
		if possible:
			answer += 1
		
	print(answer)
		
solution1(N, turns)
