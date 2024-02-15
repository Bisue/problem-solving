# 서로 다른 수
# https://study.helloalgo.co.kr/study/1019/room/602/6591

import sys

N = int(sys.stdin.readline())
kind = set(map(int, sys.stdin.readline().split()))

print(len(kind))
