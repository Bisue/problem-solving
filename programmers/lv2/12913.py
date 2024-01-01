# 땅따먹기
# https://school.programmers.co.kr/learn/courses/30/lessons/12913


def solution(land):
    scores = [[0 for _ in range(4)] for _ in range(len(land) + 1)]

    for rowIdx in range(len(land)):
        row = land[rowIdx]
        for colIdx in range(4):
            val = row[colIdx]

            prev = 0
            for prevColIdx in range(4):
                if prevColIdx == colIdx:
                    continue

                prev = max(prev, scores[rowIdx][prevColIdx])

            scores[rowIdx + 1][colIdx] += max(scores[rowIdx + 1][colIdx], prev + val)

    return max(scores[len(land)])
