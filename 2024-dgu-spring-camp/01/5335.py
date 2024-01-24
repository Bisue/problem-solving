# N번째 피보나치 수 구하기 3
# https://study.helloalgo.co.kr/study/1019/room/588/6421

n = int(input())

fiba = [1, 2, 4]
while len(fiba) < n:
    fiba.append(fiba[-1] + 2 * fiba[-2] - fiba[-3])

print(fiba[n - 1] % 1_000_000_007)
