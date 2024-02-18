// 수의 분할
// https://study.helloalgo.co.kr/study/1019/room/603/6601

#include <iostream>
#include <vector>
using namespace std;

int main() {
	int X, N;
	int nums[100];
	
	cin >> X >> N;
	for (int i=0; i<X; i++) {
		cin >> nums[i];
	}
	
	int dp[1001001];
	for (int i=0; i<X; i++) {
		dp[nums[i]] = 1;
	}
	
	for (int i=0; i<=N; i++) {
		for (int j=0; j<X; j++) {
			int num = nums[j];
			if (i - num > 0) {
				dp[i] = (dp[i] + dp[i - num]) % 1000000007;
			}
		}
	}
	
	cout << dp[N] << '\n';
	
	return 0;
}
