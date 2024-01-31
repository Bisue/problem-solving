# 선입선출
# https://study.helloalgo.co.kr/study/1019/room/593/9380/source/826101/

from collections import deque

N = int(input())
snacks = list(map(int, input().split()))

maxes = sorted(snacks, reverse=True)
maxesIdx = 0

order = 1
q = deque()
for i in range(N):
    q.append((snacks[i], i))

answer = -1
while len(q) > 0:
    while True:
        expired, idx = q.popleft()
        if expired == maxes[maxesIdx]:
            if idx == 0:
                answer = order
            order += 1
            maxesIdx += 1
            break
        else:
            q.append((expired, idx))
    if answer >= 0:
        break
        
print(answer)
