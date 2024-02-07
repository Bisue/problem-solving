// 나무 자르기
// https://study.helloalgo.co.kr/study/1019/room/598/6555

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long N, M, temp;
    cin >> N >> M;

    vector<long long> woods(N);
    for (long long i = 0; i < N; i++)
    {
        cin >> temp;
        woods[i] = temp;
    }

    long long start = 0, end = 2000000000;
    long long answer = 0;
    while (start <= end)
    {
        long long mid = (start + end) / 2;

        long long cutted = 0;
        for (long long wood : woods)
        {
            cutted += wood - mid > 0 ? wood - mid : 0;
        }

        if (cutted >= M)
        {
            answer = mid;
            start = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
    }

    cout << answer << "\n";

    return 0;
}
