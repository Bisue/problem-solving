# 회전 초밥(KOI지역2012_중등부_2)
# https://study.helloalgo.co.kr/study/1019/room/590/6449/source/826165/

import sys

N, D, K, C = map(int, input().split())
belt = []
for _ in range(N):
    belt.append(int(sys.stdin.readline().rstrip()))


# O(N*K) (but 잡다한게 많아서인지 시간초과남)
def solution1(N, D, K, C, belt):
    # 다음 초밥 index, 다음 초밥 id 반환 - O(1)
    def getNext(cur):
        # nIdx = (cur + 1)%N
        nIdx = 0 if cur == N - 1 else cur + 1
        return nIdx, belt[nIdx]

    answer = 0
    # 시작 위치 s - O(N*K)
    for s in range(N):  # O(N)
        sushi = set()  # 현재 먹은 초밥 종류
        cIdx = s
        sushi.add(belt[cIdx])  # O(1)
        picks, kind = 1, 1
        while picks < K:  # O(K)
            cIdx, cSushi = getNext(cIdx)  # O(1)
            if cSushi not in sushi:  # O(1)
                kind += 1
                sushi.add(cSushi)  # O(1)
            picks += 1

        if C not in sushi:  # O(1)
            sushi.add(C)  # O(1)
            kind += 1

        # print(s, belt[s:s+K], sushi)
        # answer = max(answer, len(sushi)) # O(D ?)
        answer = max(answer, kind)  # O(1): ~2

    print(answer)


# 깔끔한 O(NK)~
def solution2(N, D, K, C, belt):
    answer = 0
    for s in range(N):
        e = s + K
        if e > N:
            cur = set(belt[s:N] + belt[: e - N] + [C])
            answer = max(answer, len(cur))
        else:
            cur = set(belt[s:e] + [C])
            answer = max(answer, len(cur))

    print(answer)


# solution1(N, D, K, C, belt)
solution2(N, D, K, C, belt)
