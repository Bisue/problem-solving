# 동국대는 가위바위보를 좋아해
# https://study.helloalgo.co.kr/exam/618/solve/4002

"""
1. Dict(Map) 활용 구현 문제

지면 자신이 좋아하는 손 모양을 상대방을 이길 수 있는 손 모양으로 바꿈
"""

import sys

losses = {
    "paper": "scissors",
    "scissors": "rock",
    "rock": "paper",
}

wins = {
    "paper": "rock",
    "scissors": "paper",
    "rock": "scissors",
}

N, M = map(int, sys.stdin.readline().split())
prefers = {}
for _ in range(N):
    name, prefer = sys.stdin.readline().split()
    if name not in prefers:
        prefers[name] = prefer

for _ in range(M):
    name1, name2 = sys.stdin.readline().split()
    if wins[prefers[name1]] == prefers[name2]:
        prefers[name2] = losses[prefers[name1]]
    elif wins[prefers[name2]] == prefers[name1]:
        prefers[name1] = losses[prefers[name2]]

names = sorted(prefers.keys())
for name in names:
    print(name, prefers[name])
