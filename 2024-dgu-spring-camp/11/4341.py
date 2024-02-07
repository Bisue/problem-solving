# 휴게소 설치
# https://study.helloalgo.co.kr/study/1019/room/598/6559

# 휴게소가 없는 최대 길이가 x 일 때, 휴게소의 개수가 N+M개 이하인가?

N, M, L = map(int, input().split())
rests = list(map(int, input().split()))
rests.sort()

start, end = 1, L
answer = -1
while start <= end:
	mid = (start + end)//2
	
	counts = 0
	prev = 0
	for i in range(N):
		counts += (rests[i] - prev)//mid # 이전부터 자신까지 조건 채우기 위한 휴게소 수
		# 위 계산에 자기 자신이 포함 안되는 경우
		if (rests[i] - prev)%mid != 0:
			counts += 1 # 자기 자신 카운팅
		prev = rests[i]
	counts += (L - prev)//mid
	# 도로 끝은 휴게소가 없어도 됨
	if (L - prev)%mid == 0:
		counts -= 1
	
	if counts <= N+M:
		answer = mid
		end = mid - 1
	else:
		start = mid + 1
		
print(answer)
