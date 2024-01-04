// 다리를 지나는 트럭
// https://school.programmers.co.kr/learn/courses/30/lessons/42583

#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int timer = 0;
    int nextIdx = 0;
    int completed = 0;
    int curWeights = 0;
    
    queue<pair<int, int>> bridge;
    while (completed < truck_weights.size()) {
        timer++;
        
        if (timer >= bridge.front().second) {
            curWeights -= bridge.front().first;
            completed++;
            bridge.pop();
        }
        
        if (nextIdx < truck_weights.size()) {
            int nextWeights = truck_weights[nextIdx];
            if (bridge.size() < bridge_length && curWeights + nextWeights <= weight) {
                bridge.push({ nextWeights, timer + bridge_length });
                nextIdx++;
                curWeights += nextWeights;
            }
        }
    }
    
    return timer;
}
