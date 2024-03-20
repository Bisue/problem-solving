# 명제 증명
# https://www.acmicpc.net/problem/2224

import sys

# build alphas
alphas = []
for code in list(range(ord("A"), ord("Z") + 1)) + list(range(ord("a"), ord("z") + 1)):
    alphas.append(chr(code))

# alpha to index of alphas
alpha2Idx = {alphas[i]: i for i in range(len(alphas))}

N = int(sys.stdin.readline())
truth = [[False for _ in range(len(alphas))] for _ in range(len(alphas))]
for i in range(len(truth)):
    truth[i][i] = True

for _ in range(N):
    line = sys.stdin.readline().rstrip()
    p, q = line.split(" => ")

    truth[alpha2Idx[p]][alpha2Idx[q]] = True

# 플로이드 워셜
for m in range(len(truth)):
    for p in range(len(truth)):
        for q in range(len(truth)):
            if truth[p][m] and truth[m][q] and not truth[p][q]:
                truth[p][q] = True

counts = 0
answers = []
for pi in range(len(truth)):
    for qi in range(len(truth)):
        if pi == qi:
            continue

        if truth[pi][qi]:
            answers.append(f"{alphas[pi]} => {alphas[qi]}")
            counts += 1

print(counts)
print("\n".join(answers))
