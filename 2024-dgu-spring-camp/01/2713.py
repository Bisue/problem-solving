# 숫자놀이
# https://study.helloalgo.co.kr/study/1019/room/588/6422

n = int(input())
nums = list(map(int, input().split()))

nums.sort()


def getAvg(sortedNums):
    return round(sum(sortedNums) / len(sortedNums))


def getMid(sortedNums):
    return sortedNums[len(sortedNums) // 2]


def getMost(sortedNums):
    maxNum, maxCnt = 0, 0
    prev, cnt = 0, 0
    for num in sortedNums:
        if num == prev:
            cnt += 1
        else:
            if cnt >= maxCnt:
                maxNum, maxCnt = prev, cnt
            prev = num
            cnt = 1

    # [TODO] remove duplicated code
    if cnt >= maxCnt:
        maxNum, maxCnt = prev, cnt

    return maxNum


def getRange(sortedNums):
    return sortedNums[-1] - sortedNums[0]


print(getAvg(nums))
print(getMid(nums))
print(getMost(nums))
print(getRange(nums))
