# 암호 만들기
# https://www.acmicpc.net/problem/1759

L, C = map(int, input().split())
alphas = sorted(input().split())

moums = {"a", "e", "i", "o", "u"}

password = []


def printAllPassword(start, moum, jaum):
    if moum + jaum == L and moum >= 1 and jaum >= 2:
        print("".join(password))
        return

    for i in range(start + 1, C):
        password.append(alphas[i])
        if alphas[i] in moums:
            printAllPassword(i, moum + 1, jaum)
        else:
            printAllPassword(i, moum, jaum + 1)
        password.pop()


printAllPassword(-1, 0, 0)
