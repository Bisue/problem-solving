// 베스트앨범
// https://school.programmers.co.kr/learn/courses/30/lessons/42579

/*
베스트 앨범: 장르 별로 가장 많이 재새된 노래 2개씩 모은 것
장르 순서: 속한 노래(전체)가 많이 재생된 장르 순(sum)
장르 내 노래 순: 많이 재생된 노래 순(내림) / 같으면 고유 번호가 낮은 순(오름)
*/

#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <tuple>

using namespace std;

bool compareMusic(const tuple<int, int, string>& a, const tuple<int, int, string>& b) {
    if (get<1>(a) != get<1>(b)) {
        return get<1>(a) > get<1>(b);
    } else {
        return get<0>(a) < get<0>(b);
    }
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<tuple<int, int, string>> musics;
    
    for (int idx = 0; idx < genres.size(); idx++) {
        string genre = genres[idx];
        int play = plays[idx];
        
        musics.push_back({ idx, play, genre });
    }
    
    sort(musics.begin(), musics.end(), compareMusic);
    
    unordered_map<string, vector<pair<int, int>>> genrePicks;
    unordered_map<string, int> genreSums;
    for (const tuple<int, int, string>& m: musics) {
        int idx = get<0>(m);
        int play = get<1>(m);
        string genre = get<2>(m);
        
        if (genrePicks.find(genre) == genrePicks.end()) {
            genrePicks[genre] = vector<pair<int, int>>();
        }
        
        if (genrePicks[genre].size() < 2) {
            genrePicks[genre].push_back({ idx, play });
        }
        genreSums[genre] += play;
    }
    
    vector<string> genreOrders;
    for (const auto& it: genreSums) {
        genreOrders.push_back(it.first);
    }
    
    sort(genreOrders.begin(), genreOrders.end(), [genreSums](const string& a, const string& b) ->bool {
        return genreSums.at(a) > genreSums.at(b);
    });
    
    vector<int> answer;
    for (const string& genre: genreOrders) {
        for (const pair<int, int>& music: genrePicks[genre]) {
            answer.push_back(get<0>(music));
        }
    }
    
    return answer;
}
