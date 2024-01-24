# N번째 피보나치 수 구하기 1
# https://study.helloalgo.co.kr/study/1019/room/588/6417/source/822966/

n = int(input())


def solution1(n):
    cache = {}

    def fibo(num):
        if num in cache:
            return cache[num]

        if num == 1:
            return 1
        elif num == 2:
            return 1

        result = fibo(num - 1) + fibo(num - 2)
        cache[num] = result
        return result

    print(fibo(n))


def solution2(n):
    fibo = [0 for _ in range(n + 1)]

    fibo[1], fibo[2] = 1, 1

    for i in range(3, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    print(fibo[n])


# solution1(n)
solution2(n)
