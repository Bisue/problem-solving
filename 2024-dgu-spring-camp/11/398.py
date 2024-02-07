# 수 찾기
# https://study.helloalgo.co.kr/study/1019/room/598/6553

N, M = map(int, input().split())
nums = list(map(int, input().split()))
targets = list(map(int, input().split()))

def findNum(n, arr, target):
    start, end = 0, n-1
    answer = None
    while start <= end:
        mid = (start + end)//2
        
        if arr[mid] == target:
            answer = mid
            return True
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
            
    return False

for target in targets:
    print('1' if findNum(N, nums, target) else '0')
