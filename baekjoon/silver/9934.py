# 완전 이진 트리
# https://www.acmicpc.net/problem/9934

"""
단순히 트리를 역으로 채우는 문제
"""

K = int(input())
buildings = list(map(int, input().split()))

tree = [0 for _ in range(2**K)]  # 1~
leafBase = 2 ** (K - 1)

idx = 0


def fillTree(cur):
    global idx

    left, right = cur * 2, cur * 2 + 1
    if left < len(tree):
        fillTree(left)

    tree[cur] = buildings[idx]
    idx += 1

    if right < len(tree):
        fillTree(right)


fillTree(1)

idx = 1
for depth in range(K):
    for i in range(2**depth):
        print(tree[idx], end=" ")
        idx += 1
    print()
