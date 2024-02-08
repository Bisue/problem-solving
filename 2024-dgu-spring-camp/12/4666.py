# 수 정렬하기
# https://study.helloalgo.co.kr/study/1019/room/599/6565

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
print('\n'.join(map(str, nums)))
