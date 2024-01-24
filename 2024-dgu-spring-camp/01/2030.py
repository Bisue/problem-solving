# 로마 카톨릭 미사(COCI_2013_CONTEST2_2)
# https://study.helloalgo.co.kr/study/1019/room/588/6414

dirs = [
    (-1, 0),
    (0, -1),
    (-1, -1),
    (1, 0),
    (0, 1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

r, s = map(int, input().split())
benches = []
for _ in range(r):
    benches.append(list(input()))


def isValid(x, y):
    return 0 <= x < r and 0 <= y < s


visited = {(x, y): set() for x in range(r) for y in range(s)}


def countAroundAll(x, y):
    result = 0

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if isValid(nx, ny) and benches[nx][ny] == "o":
            result += 1

    return result


def handshake(x, y):
    result = 0

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if (
            isValid(nx, ny)
            and benches[nx][ny] == "o"
            and (nx, ny) not in visited[(x, y)]
        ):
            visited[(nx, ny)].add((x, y))
            result += 1

    return result


answer = 0

maxVal = 0
maxX, maxY = None, None
for x in range(r):
    for y in range(s):
        if benches[x][y] == "o":
            continue

        cur = countAroundAll(x, y)
        if cur > maxVal:
            maxVal = cur
            maxX, maxY = x, y

if maxVal > 0:
    benches[maxX][maxY] = "o"

for x in range(r):
    for y in range(s):
        if benches[x][y] == "o":
            shakes = handshake(x, y)
            answer += shakes

print(answer)
