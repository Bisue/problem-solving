// 돈 만들기
// https://study.helloalgo.co.kr/study/1019/room/603/6602

#include <iostream>
#include <algorithm>
#define INT_MAX 2147483647
using namespace std;

int dp[1000001];

int main() {
	int X, N;
	int coins[100];
	
	cin >> X >> N;
	for (int i=0; i<=N; i++) {
		dp[i] = INT_MAX;
	}
	
	for (int i=0; i<X; i++) {
		cin >> coins[i];
		dp[coins[i]] = 1;
	}
	
	for (int i=1; i<=N; i++) {
		if (dp[i] < INT_MAX) continue;
		
		for (int j=0; j<X; j++) {
			if (i - coins[j] > 0) {
				dp[i] = min(dp[i], dp[i - coins[j]]);
			}
		}
		
		if (dp[i] < INT_MAX) {
			dp[i]++;
		}
	}
	
	if (dp[N] == INT_MAX) {
		cout << -1 << '\n';
	} else {
		cout << dp[N] << '\n';
	}
	
	
	return 0;
}
