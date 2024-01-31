# 조세퍼스 문제
# https://study.helloalgo.co.kr/study/1019/room/593/6480/source/826052/

from collections import deque

N, M = map(int, input().split())
q = [ i for i in range(1, N+1) ]
curIdx = 0
answer = []
while len(q) > 0:
    curIdx += M - 1 # 0: 1, 1: 2, 2: "3", ...
    while curIdx >= len(q):
        curIdx -= len(q) # effective mod?
    
    answer.append(q.pop(curIdx)) # O(N) ~~ len(q)
    
print(' '.join(map(str, answer)))
