// 기능개발
// https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=cpp

#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

void elapsed(vector<int> &progresses, vector<int> &speeds)
{
    for (int i = 0; i < progresses.size(); i++)
    {
        progresses[i] += speeds[i];
    }
}

vector<int> solution(vector<int> progresses, vector<int> speeds)
{
    vector<int> answer;
    int curIdx = 0;

    while (curIdx < progresses.size())
    {
        elapsed(progresses, speeds);

        int completed = 0;
        for (int i = curIdx; i < progresses.size(); i++)
        {
            if (progresses[i] < 100)
                break;

            completed++;
        }

        if (completed > 0)
        {
            curIdx += completed;
            answer.push_back(completed);
        }
    }

    return answer;
}
