# 정수 제곱근
# https://www.acmicpc.net/problem/2417

N = int(input())

s, e = 0, N

answer = 0
while s<=e:
    m = (s+e)//2
    
    if m*m >= N:
        answer = m
        e = m - 1
    else:
        s = m + 1
        
print(answer)
