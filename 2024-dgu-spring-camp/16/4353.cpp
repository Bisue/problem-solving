// 제곱수의 합
// https://study.helloalgo.co.kr/study/1019/room/603/6603

#include <iostream>
#define INT_MAX 2147483647
using namespace std;

int dp[100001];

int main() {
	int N;
	cin >> N;
	
	for (int i=0; i<=N; i++) {
		dp[i] = INT_MAX;
	}
	
	for (int i=1; i*i<=N; i++) {
		dp[i*i] = 1;
	}
	
	for (int i=1; i<=N; i++) {
		if (dp[i] < INT_MAX) continue;
		
		for (int j=1; j*j<=i; j++) {
			int sq = j*j;
			if (i - sq > 0) {
				dp[i] = min(dp[i], dp[i - sq] + 1);
			}
		}
	}
	
	cout << dp[N] << '\n';
}
