# 분수 비교하기
# https://study.helloalgo.co.kr/study/1019/room/588/6418

a, b, c, d = map(int, input().split())

# [TIP] 실수 비교 연산을 피하기 위해
# 통분 처리한 분자를 비교
num1, num2 = a * d, c * b

if num1 > num2:
    print("A/B")
elif num1 < num2:
    print("C/D")
else:
    print("EQUALS")
