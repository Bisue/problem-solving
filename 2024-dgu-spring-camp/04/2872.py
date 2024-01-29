# 0을 만들자
# https://study.helloalgo.co.kr/study/1019/room/591/6463

N = int(input())

answer = 0
operations = []


def dfs(num):
    if num >= N:
        tempSt = []  # ' ' operator가 전처리된 연산 스택
        tempBuffer = 0  # ' ' operator를 위한 버퍼 정수

        # ' ' operator 전처리
        for i in range(1, N + 1):
            if tempBuffer > 0:
                tempSt.append(tempBuffer * 10 + i)
                tempBuffer = 0
            else:
                tempSt.append(i)

            if i < N:
                if operations[i - 1] == " ":
                    tempBuffer = tempSt.pop()
                else:
                    tempSt.append(operations[i - 1])

        # 전처리된 연산 계산
        result = tempSt[0]
        for i in range(1, len(tempSt) - 1, 2):
            if tempSt[i] == "+":
                result += tempSt[i + 1]
            else:
                result -= tempSt[i + 1]

        if result == 0:
            for i in range(1, N + 1):
                print(i, end="")
                if i < N:
                    print(operations[i - 1], end="")
            print()
        return

    # print(num, operations)

    for oper in [" ", "+", "-"]:
        operations.append(oper)
        dfs(num + 1)
        operations.pop()


dfs(1)
