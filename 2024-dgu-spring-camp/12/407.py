# 과정 출력하기(삽입)
# https://study.helloalgo.co.kr/study/1019/room/599/6564/source/828553/

N = int(input())
nums = list(map(int, input().split()))

print(' '.join(map(str, nums)))
for i in range(1, N):
    pos = i
    for j in range(1, i+1):
        targetPos = i-j
        if nums[pos] < nums[targetPos]:
            nums[pos], nums[targetPos] = nums[targetPos], nums[pos]
            pos = targetPos
            print(' '.join(map(str, nums)))
    