# N번째 피보나치 수 구하기 2
# https://study.helloalgo.co.kr/study/1019/room/588/6420

n = int(input())

fibo = [1, 1]

# [TIP] python은 노상관이지만,
# cpp 등으로 할 경우 중간값 범위 조심
while len(fibo) < n:
    fibo.append(fibo[-2] + fibo[-1])

print(fibo[-1] % 1_000_000_007)
