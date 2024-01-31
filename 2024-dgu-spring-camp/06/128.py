# 카드
# https://study.helloalgo.co.kr/study/1019/room/593/9382/source/826111/

from collections import deque

N = int(input())
cards = deque([ i for i in range(1, N+1) ])

throwTurn = True
while len(cards) > 1:
    if throwTurn:
        cards.popleft()
    else:
        cards.append(cards.popleft())
        
    throwTurn = not throwTurn
    
print(cards[0])
