# 3이하로 분할하기
# https://study.helloalgo.co.kr/study/1019/room/603/6600

"""
dp[N]: dp[N-1] + 1
     : dp[N-2] (+ 11) + 2
	 : dp[N-3] (+ 111) (+ 12) (+ 21) + 3
"""

"""
1
1


2
1 1
2


3
1 1 1
1 2
2 1
3


4
1 1 1 1 (3)
1 1 2 (2)
1 2 1 (3)
2 1 1 (3)
2 2 (original)
1 3 (1)
3 1 (3)


5

1 1 1 1 1 (4)
1 1 1 2 (3)
1 1 2 1 (4)
1 2 1 1 (4)
2 1 1 1 (4)
1 2 2 (3)
2 1 2 (3)
2 2 1 (4)
1 1 3 (3)
1 3 1 (4)
3 1 1 (4)
2 3 (3)
3 2 (3)
"""

import sys

dp = [0 for _ in range(200)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for i in range(5, 200):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline())

    print(dp[n])
