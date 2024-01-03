// 프로세스
// https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=cpp

#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location)
{
    vector<int> sortedPriorities(priorities);
    sort(sortedPriorities.begin(), sortedPriorities.end(), greater<int>());

    int priorIdx = 0;
    int nowIdx = 0;
    int orderCnt = 0;
    while (true)
    {
        if (priorities[nowIdx] == sortedPriorities[priorIdx])
        {
            orderCnt++;
            priorIdx++;
            if (nowIdx == location)
            {
                return orderCnt;
            }
        }
        nowIdx = (nowIdx + 1) % priorities.size();
    }
}
