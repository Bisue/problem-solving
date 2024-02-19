// 욕심많은 윌리
// https://study.helloalgo.co.kr/study/1019/room/604/6613

/*
dp[x]: 무게 x 까지의 최대 물품 가치
dp[i][x]: 1~i 까지 물건으로 무게 x 까지의 최대 물품 가치
dp[i][x] = max(dp[i-1][w], dp[i-1][w - wi] + vi)
*/

#include <iostream>
#include <algorithm>
using namespace std;

int objs[101][2];
long long dp[101][100001];

int main()
{
	int N, W;
	cin >> N >> W;

	objs[0][0] = 0;
	objs[0][1] = 0;
	for (int i = 1; i <= N; i++)
	{
		cin >> objs[i][0] >> objs[i][1];
	}

	for (int i = 1; i <= N; i++)
	{
		for (int j = 0; j <= W; j++)
		{
			dp[i][j] = dp[i - 1][j];

			int wi = objs[i][0];
			int vi = objs[i][1];

			// cout << i << ", " << j << ", " << wi << ", " << vi << "\n";
			if (j - wi >= 0)
			{
				// cout << " - " << dp[i][j] << ", " << dp[i-1][j-wi] << ", " << vi << ", " << dp[i-1][j-wi] + vi << "\n";
				dp[i][j] = max(dp[i][j], dp[i - 1][j - wi] + vi);
			}
		}
	}

	/*
	for (int i=1; i<=N; i++) {
		for (int j=0; j<=W; j++) {
			cout << dp[i][j] << " ";
		}
		cout << '\n';
	}
	*/

	cout << dp[N][W] << endl;

	return 0;
}
