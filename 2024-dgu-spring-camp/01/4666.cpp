// 수 정렬하기
// https://study.helloalgo.co.kr/study/1019/room/588/6416/source/822943/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    int n, temp;
    vector<int> nums;
    
    cin >> n;
    
    for (int i=0; i<n; i++) {
        cin >> temp;
        nums.push_back(temp);
    }
    
    sort(nums.begin(), nums.end());
        
    for (int num: nums) {
        cout << num << '\n';
    }
    
    return 0;
}
