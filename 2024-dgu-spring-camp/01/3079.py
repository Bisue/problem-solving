# 약수의 합
# https://study.helloalgo.co.kr/study/1019/room/588/6411

n = int(input())

answer = 0
# O(제곱근연산 + 루트N)
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        answer += i
        if n // i != i:
            answer += n // i

print(answer)
