# 수 정렬하기
# https://study.helloalgo.co.kr/study/1019/room/588/6416/source/822943/

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()

for num in nums:
    print(num)
