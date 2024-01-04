// 디스크 컨트롤러
// https://school.programmers.co.kr/learn/courses/30/lessons/42627

#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> jobs) {
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    sort(jobs.begin(), jobs.end(), [](const vector<int>& a, const vector<int>& b) ->bool {
        return a[0] < b[0];
    });
    
    int jobsIdx = 0;
    int timer = 0;
    int nextRelease = 0;
    int completed = 0;
    int avg = 0;
    int begin = 0;
    while (completed <= jobs.size()) {
        while (jobsIdx < jobs.size() && jobs[jobsIdx][0] <= timer) {
            pq.push({ jobs[jobsIdx][1], jobs[jobsIdx][0] });
            jobsIdx++;
        }
        
        // cout << "timer: " << timer << ", queue size: " << pq.size() << endl;
        
        if (timer == nextRelease) {
            completed++;
            
            avg += timer - begin;
        }
        
        if (timer >= nextRelease && !pq.empty()) {
            pair<int, int> next = pq.top();
            pq.pop();
            
            nextRelease = timer + next.first;
            
            // cout << "- completed!" << endl;
            // cout << "- next: " << next.first << " / release: " << nextRelease << endl;
            
            // cout << "- begin: " << begin << " / duration: " << timer - begin << endl;
            
            begin = next.second;
        }
        
        timer++;
    }
    
    // cout << avg << endl;
    
    return avg / (completed - 1);
}
