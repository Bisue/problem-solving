# ALPS식 투표(COCI_2011_CONTEST3_2)
# https://study.helloalgo.co.kr/study/1019/room/588/6415

X = int(input())
N = int(input())

threshold = int(X * 0.05)

candidates = []

chips = {}
allScores = []
for _ in range(N):
    name, vote = input().split()
    vote = int(vote)

    if vote < threshold:
        continue

    candidates.append(name)
    chips[name] = 0

    for i in range(1, 15):
        allScores.append((name, vote / i))

allScores.sort(key=lambda s: s[1], reverse=True)
for i in range(14):
    name, _ = allScores[i]
    chips[name] += 1

candidates.sort()
for name in candidates:
    print(f"{name} {chips[name]}")
