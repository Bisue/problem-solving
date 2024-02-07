# 얼음 나눠주기
# https://study.helloalgo.co.kr/study/1019/room/598/6557/source/828462/

import sys

# 얼음 크기가 x 일때, N명에게 정확히 x 씩 줄 수 있는가
# - 얼음
N, M = map(int, input().split())
ices = []
for _ in range(M):
    ices.append(int(sys.stdin.readline()))

start, end = min(ices), max(ices)
answer = -1
while start <= end:
    mid = (start + end)//2
    
    cnt = 0
    for ice in ices:
        cnt += ice//mid
    
    if cnt >= N:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)
