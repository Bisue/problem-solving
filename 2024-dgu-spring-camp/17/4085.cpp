// 서점
// https: // study.helloalgo.co.kr/study/1019/room/604/6614

/*
dp[i][x]: x의 자금으로 1~i 번째 책들로 살 수 있는 최대 페이지 수
dp[i][x] = max(dp[i-1][x], dp[i-1][x-pri] + pai)
(dp[i-1][x]: i 번째 책을 사지 않을 때)
(dp[i-1][x-pri] + pai: i 번째 책을 살 때)
*/

#include <iostream>
#include <algorithm>
using namespace std;

int prices[1001];
int pages[1001];
int dp[1001][100001];

int main()
{
    int N, X;
    cin >> N >> X;

    for (int i = 1; i <= N; i++)
    {
        cin >> prices[i];
    }
    for (int i = 1; i <= N; i++)
    {
        cin >> pages[i];
    }

    for (int i = 1; i <= N; i++)
    {
        for (int x = 0; x <= X; x++)
        {
            dp[i][x] = dp[i - 1][x];
            if (x - prices[i] >= 0)
            {
                dp[i][x] = max(dp[i][x], dp[i - 1][x - prices[i]] + pages[i]);
            }
        }
    }

    cout << dp[N][X] << '\n';
}
