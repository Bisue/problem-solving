// 얼음 나눠주기
// https://study.helloalgo.co.kr/study/1019/room/598/6557

#include <iostream>
#include <vector>
using namespace std;

int N, M;
vector<int> ices;

int main()
{
    cin >> N >> M;

    int temp;
    for (int i = 0; i < M; i++)
    {
        cin >> temp;
        ices.push_back(temp);
    }

    int start = 1, end = 1000000000;
    int answer = -1;
    while (start <= end)
    {
        int mid = (start + end) / 2;

        int cnt = 0;
        for (int ice : ices)
        {
            cnt += ice / mid;
        }

        if (cnt >= N)
        {
            answer = mid;
            start = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
    }

    cout << answer << '\n';
}
