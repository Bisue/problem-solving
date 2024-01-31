# 소수 경로
# https://study.helloalgo.co.kr/study/1019/room/593/6482/source/826090/

from collections import deque

T = int(input())


def checkPrime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


for _ in range(T):
    start, end = map(int, input().split())
    
    q = deque()
    q.append((start, 0, [start]))
    visited = [False for _ in range(10000)]
    answer = -1
    
    while len(q) > 0:
        cur, tries, route = q.popleft()
        
        if cur == end:
            answer = tries
            break
            
        for i in range(10):
            for nxt in [cur%1000 + i*1000, (cur//1000)*1000 + cur%100 + i*100, (cur//100)*100 + cur%10 + i*10, (cur//10)*10 + i]:
                if nxt < 1000:
                    continue
                if not visited[nxt] and checkPrime(nxt):
                    q.append((nxt, tries + 1, route + [nxt]))
                    visited[nxt] = True
                              
    if answer >= 0:
        print(answer)
    else:
        print('Impossible')
