// 약수의 합
// https://study.helloalgo.co.kr/study/1019/room/588/6411

#include <iostream>
#include <cmath>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	long long n;
	long long answer = 0;
	
	cin >> n;
	
	for (long long i=1; i*i<=n; i++) {
		if (n % i == 0) {
			answer += i;
			if (n / i != i) {
				answer += (long long)(n / i);
			}
		}
	}
	
	cout << answer << endl;
	
	return 0;
}
