# 숫자 카드
# https://www.acmicpc.net/problem/10815

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

cards.sort()

answers = []
for target in targets:
    idx = -1
    s, e = 0, N-1
    while s <= e:
        m = (s + e)//2
        
        if cards[m] == target:
            idx = M
            break
        elif cards[m] > target:
            e = m - 1
        else:
            s = m + 1
    
    answers.append(0 if idx < 0 else 1)
    
print(' '.join(map(str, answers)))
