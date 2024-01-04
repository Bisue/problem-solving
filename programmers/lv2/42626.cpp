// 더 맵게
// https://school.programmers.co.kr/learn/courses/30/lessons/42626

#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int s: scoville) {
        pq.push(s);
    }
    
    int answer = 0;
    int pick = -1;
    while (!pq.empty()) {
        int now = pq.top();
        pq.pop();
        
        if (pick == -1 && now >= K) {
            return answer;
        }
        
        if (pick != -1) {
            pq.push(pick + now*2);
            pick = -1;
            answer += 1;
        } else {
            pick = now;
        }
    }
    
    return -1;
}
