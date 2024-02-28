# 소수 구하기
# https://www.acmicpc.net/problem/1929

N, M = map(int, input().split())

primes = [True for _ in range(M + 1)]
primes[1] = False
for i in range(2, M + 1):
    if not primes[i]:
        continue

    factor = 2
    while i * factor <= M:
        primes[i * factor] = False

        factor += 1

for i in range(N, M + 1):
    if primes[i]:
        print(i)
