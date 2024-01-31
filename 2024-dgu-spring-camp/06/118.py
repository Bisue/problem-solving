# 정수 배열이 너무 좋아
# https://study.helloalgo.co.kr/study/1019/room/593/9381/source/826105/

from collections import deque

N = int(input())
nums = list(map(int, input().split()))
keys = list(input())

dq = deque(nums)
isQueue = True
for key in keys:
    if key == 'R':
        isQueue = not isQueue
    else:
        if len(dq) == 1: # 문제 조건?
            print('Error')
            exit(0)
        if isQueue:
            dq.popleft()
        else:
            dq.pop()
            
while len(dq) > 0:
    if isQueue:
        print(dq.popleft(), end=" ")
    else:
        print(dq.pop(), end=" ")
print()
