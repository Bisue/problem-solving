# 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729

"""
내 풀이는 메모이제이션을 사용하지 않은 풀이.

백준 다른 풀이를 보면 보통 메모이제이션을 사용한 풀이가 대부분임

이 문제에서는 N이 충분히 작아서 괜찮았던 것 같은데
더 커지면 메모이제이션을 고려해야 할 듯.
"""

N = int(input())


def printHanoi(n, s, e):
    if n == 1:
        print(s, e)
        return

    printHanoi(n - 1, s, 6 - s - e)
    print(s, e)
    printHanoi(n - 1, 6 - s - e, e)


print(2**N - 1)
printHanoi(N, 1, 3)
