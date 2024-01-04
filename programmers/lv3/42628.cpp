// 이중우선순위큐
// https://school.programmers.co.kr/learn/courses/30/lessons/42628

#include <string>
#include <vector>
#include <queue>
#include <sstream>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> operations) {
    priority_queue<int> maxPq;
    priority_queue<int, vector<int>, greater<int>> minPq;
    
    int minDel = 0, maxDel = 0;
    
    for (const string& operation: operations) {
        stringstream ss(operation);
        char command;
        int num;
        
        ss >> command >> num;
        
        if (command == 'I') {
            minPq.push(num);
            maxPq.push(num);
        } else if (command == 'D' && num == 1) {
            if (maxPq.size() - minDel <= 0) {
                continue;
            }
            
            maxPq.pop();
            maxDel++;
        } else if (command == 'D' && num == -1) {
            if (minPq.size() - maxDel <= 0) {
                continue;
            }
            
            minPq.pop();
            minDel++;
        }
        
        // 중간에 큐가 비어버리는 경우 예외처리 (초기화)
        if (minPq.size() - maxDel == 0 && maxPq.size() - minDel == 0) {
            minPq = priority_queue<int, vector<int>, greater<int>>();
            maxPq = priority_queue<int>();
            minDel = 0;
            maxDel = 0;
        }
    }
    
    vector<int> answer = { 0, 0 };
    if (minPq.size() - maxDel == 1) {
        int remained;
        if (minDel > maxDel) {
            remained = maxPq.top();
        } else {
            remained = minPq.top();
        }
        answer[0] = remained;
        answer[1] = remained;
    } else if (minPq.size() - maxDel >= 2) {
        answer[0] = maxPq.top();
        answer[1] = minPq.top();
    }
    
    return answer;
}
