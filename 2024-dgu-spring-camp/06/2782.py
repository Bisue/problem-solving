# 방금건 취소
# https://study.helloalgo.co.kr/study/1019/room/593/6479/source/823527/

K = int(input())

st = []
for _ in range(K):
    num = int(input())
    if num > 0:
        st.append(num)
    elif len(st) > 0:
        st.pop()

print(sum(st))
