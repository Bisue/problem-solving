// 의상
// https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=cpp

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    unordered_map<string, int> partCounts;
    
    for (auto& cloth: clothes) {
        partCounts[cloth[1]]++;
    }
    
    int possibles = 1;
    for (auto& pair: partCounts) {
        possibles *= pair.second + 1;
    }
    
    return possibles - 1;
}
