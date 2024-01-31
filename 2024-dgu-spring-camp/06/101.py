# 스택
# https://study.helloalgo.co.kr/study/1019/room/593/6477/source/826023/

st = []

while True:
    tokens = input().split()
    if tokens[0] == 'push':
        num = int(tokens[1])
        print(num)
        st.append(num)
    elif tokens[0] == 'pop':
        if len(st) == 0:
            print(-1)
            continue
        
        print(st.pop())
    elif tokens[0] == 'size':
        print(len(st))
    elif tokens[0] == 'empty':
        print(1 if len(st) == 0 else 0)
    elif tokens[0] == 'top':
        if len(st) == 0:
            print(-1)
            continue
        
        print(st[-1])
    elif tokens[0] == 'end':
        break
