// LCS 3
// https://study.helloalgo.co.kr/study/1019/room/604/6618/source/831116/

/*
dp[i-1][j-1][k], dp[i-1][j][k-1], dp[i][j-1][k-1]
들은 비교할 필요가 없나?
-> 찾아보기
*/

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int dp[101][101][101];

int main() {
	string A, B, C;
	cin >> A;
	cin >> B;
	cin >> C;
	
	int lA = A.size(), lB = B.size(), lC = C.size();
	
	for (int i=1; i<=lA; i++) {
		for (int j=1; j<=lB; j++) {
			for (int k=1; k<=lC; k++) {
				if (A[i-1] == B[j-1] && B[j-1] == C[k-1]) {
					dp[i][j][k] = dp[i-1][j-1][k-1] + 1;
				} else {
					dp[i][j][k] = max({ dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1], dp[i-1][j-1][k], dp[i-1][j][k-1], dp[i][j-1][k-1] });
				}
			}
		}
	}
	
	cout << dp[lA][lB][lC] << '\n';
	
	return 0;
}
