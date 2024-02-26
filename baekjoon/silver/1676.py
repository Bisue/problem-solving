# 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

"""
파이썬이라서 편한 문제
"""

N = int(input())

fact = [0 for _ in range(N + 1)]
fact[0] = 1
if len(fact) > 1:
    fact[1] = 1
for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i

answer = 0

target = str(fact[N])
for i in range(len(target) - 1, -1, -1):
    if target[i] == "0":
        answer += 1
    else:
        break

print(answer)
