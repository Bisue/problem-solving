# 숫자카드뭉치
# https://study.helloalgo.co.kr/study/1019/room/602/6594

N = int(input())
cards = list(map(int, input().split()))
cardCounts = {}
for card in cards:
	if card not in cardCounts:
		cardCounts[card] = 0
	cardCounts[card] += 1
	
M = int(input())
queries = list(map(int, input().split()))
answers = []
for query in queries:
	if query not in cardCounts:
		answers.append('0')
		continue
		
	answers.append(str(cardCounts[query]))

print(' '.join(answers))

