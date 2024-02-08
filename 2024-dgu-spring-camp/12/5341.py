# 분할정복으로 별 직기
# https://study.helloalgo.co.kr/study/1019/room/599/6566/source/828556/

N = int(input())
display = [[' ' for _ in range(N)] for _ in range(N)]

def fill(n, sx, sy):
    if n == 3:
        for x in range(3):
            for y in range(3):
                if not (x == 1 and y == 1):
                    display[sx+x][sy+y] = '*'    
        return
    
    nextN = n//3
    unit = nextN
    
    for x in range(3):
        for y in range(3):
            if not (x == 1 and y == 1):
                fill(nextN, sx+x*unit, sy+y*unit)
    
fill(N, 0, 0)

for row in display:
    print(''.join(row))
