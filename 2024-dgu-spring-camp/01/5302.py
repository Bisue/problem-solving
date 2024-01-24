# 구간의 합들
# https://study.helloalgo.co.kr/study/1019/room/588/6423

n, m = map(int, input().split())
nums = list(map(int, input().split()))

sums = [0 for _ in range(n + 1)]

for i in range(n):
    sums[i + 1] = sums[i] + nums[i]

# sums[i+1]: nums[0] ~ nums[i] 까지의 합

answer = 0
for i in range(n):
    for j in range(i, n):
        if sums[j + 1] - sums[i] == m:
            answer += 1

print(answer)
