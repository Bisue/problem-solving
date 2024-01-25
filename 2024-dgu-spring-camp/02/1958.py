# 멀티그램(COCI_2016_CONTEST5_2)
# https://study.helloalgo.co.kr/study/1019/room/589/6452

target = input()

def countChars(s):
	counts = {}
	for ch in s:
		if ch not in counts:
			counts[ch] = 0
		counts[ch] += 1
	return counts

def checkCountEquals(c1, c2):
	for k in c1:
		if k not in c2 or c1[k] != c2[k]:
			return False
	
	return len(c1.keys()) == len(c2.keys())

# target을 i(1, 2, 3, ...)의 동일한 길이로 분할
# 서로 애너그램이려면, 각 gram의 알파벳 counts가 같아야 함
# 1글자 단위까지 쪼개면서 check ([TODO] 최적화: 1글자부터 올라가면서 break)

answer = -1

gramLength = len(target)
for i in range(2, len(target)+1):
	if len(target)%i != 0:
		continue
	gramLength = len(target)//i
	
	grams = []
	for i in range(len(target)//gramLength):
		grams.append(target[i*gramLength:(i+1)*gramLength])
	
	impossible = False
	counts = countChars(grams[0])
	for i in range(1, len(grams)):
		now = countChars(grams[i])
		if not checkCountEquals(counts, now):
			# print(grams, grams[i], counts, now)
			impossible = True
			break
	
	if impossible:
		continue
	else:
		answer = grams[0]
		
print(answer)
