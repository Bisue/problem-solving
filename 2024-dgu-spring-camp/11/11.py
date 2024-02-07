# 나무 자르기
# https://study.helloalgo.co.kr/study/1019/room/598/6555

N, M = map(int, input().split())
woods = list(map(int, input().split()))

start, end = 0, max(woods)
answer = 0
while start <= end:
    mid = (start + end)//2 # 현재 절단기 설정 높이
    
    cutted = 0 # 현재 가져가는 나무의 양
    for wood in woods:
        cutted += max(0, wood - mid)
    
    if cutted >= M:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)
