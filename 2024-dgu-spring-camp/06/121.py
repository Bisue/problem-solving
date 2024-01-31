# 직접 만든 큐
# https://study.helloalgo.co.kr/study/1019/room/593/6478/source/826024/

# 1. deque 
from collections import deque

q = deque()

N = int(input())
for _ in range(N):
    tokens = input().split()
    if tokens[0] == 'push':
        num = int(tokens[1])
        q.append(num)
    elif tokens[0] == 'pop':
        print(-1 if len(q) == 0 else q.popleft())
    elif tokens[0] == 'size':
        print(len(q))
    elif tokens[0] == 'empty':
        print(1 if len(q) == 0 else 0)
    elif tokens[0] == 'front':
        print(-1 if len(q) == 0 else q[0])
    elif tokens[0] == 'back':
        print(-1 if len(q) == 0 else q[-1])
