# 베스트앨범
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

"""
베스트 앨범: 장르 별로 가장 많이 재새된 노래 2개씩 모은 것
장르 순서: 속한 노래(전체)가 많이 재생된 장르 순(sum)
장르 내 노래 순: 많이 재생된 노래 순(내림) / 같으면 고유 번호가 낮은 순(오름)
"""


def solution(genres, plays):
    musics = []
    for idx in range(len(genres)):
        genre, play = genres[idx], plays[idx]

        musics.append((idx, play, genre))

    musics.sort(key=lambda m: (-m[1], m[0]))

    genrePicks = {}
    genreSums = {}
    for m in musics:
        idx, play, genre = m

        if genre not in genrePicks:
            genrePicks[genre] = []
            genreSums[genre] = 0

        if len(genrePicks[genre]) < 2:
            genrePicks[genre].append((idx, play))
        genreSums[genre] += play

    genreOrders = sorted(genreSums.items(), key=lambda e: (e[1]), reverse=True)

    answer = []
    for genre in genreOrders:
        for music in genrePicks[genre[0]]:
            answer.append(music[0])

    return answer
