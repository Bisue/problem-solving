# 주사위 고르기(2024 KAKAO WINTER INTERMSHIP)
# https://school.programmers.co.kr/learn/courses/30/lessons/258709
# (실제 코테에서 냈던 코드)

from itertools import combinations, product

casesCache = {}

def buildCases(diceList, pick):
    if pick in casesCache: return casesCache[pick]

    dices = list(map(lambda i: diceList[i], pick))
    cases = list(map(lambda p: sum(p), product(*dices)))

    casesDict = {}
    for case in cases:
        if case not in casesDict:
            casesDict[case] = 0
        casesDict[case] += 1

    casesCache[pick] = casesDict
    return casesDict


def calcWins(casesDict1, casesDict2):
    sortedVal1 = sorted(casesDict1.keys(), reverse=True)
    sortedVal2 = sorted(casesDict2.keys())

    wins = 0
    for i in range(len(sortedVal1)):
        for j in range(len(sortedVal2)):
            if sortedVal1[i] > sortedVal2[j]:
                wins += casesDict1[sortedVal1[i]] * casesDict2[sortedVal2[j]]

    return wins


def solution(dice):
    diceIndexes = set(range(len(dice)))
    picks = list(combinations(diceIndexes, len(dice) // 2))
    opponentPicks = []
    for pick in picks:
        opponentPicks.append(tuple(diceIndexes.difference(pick)))

    answer = (None, 0)
    for i in range(len(picks)):
        cases = buildCases(dice, picks[i])
        opponentCases = buildCases(dice, opponentPicks[i])

        wins = calcWins(cases, opponentCases)
        if answer[1] < wins:
            answer = (picks[i], wins)

    return list(map(lambda i: i+1, answer[0]))
