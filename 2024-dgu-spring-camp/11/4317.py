# 인강
# https://study.helloalgo.co.kr/study/1019/room/598/6560

# usb 크기가 x 일때, N개의 수업을 M개의 usb에 넣을 수 있는가? 

N, M = map(int, input().split())
videos = list(map(int, input().split()))

def isPossible(x, videos, m):
	usbNeed = 1
	curDisk = 0
	for length in videos:
		if curDisk + length > x:
			usbNeed += 1
			curDisk = length
		else:
			curDisk += length
	
	return usbNeed <= m

# usb 크기는 적어도 가장 긴 강의를 담을 수 있어야 함
start, end = max(videos), sum(videos)
while start <= end:
	mid = (start + end)//2
	
	if isPossible(mid, videos, M):
		answer = mid
		end = mid - 1
	else:
		start = mid + 1
		
print(answer)
