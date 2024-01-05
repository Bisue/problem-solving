// 가장 큰 정사각형 찾기
// https://school.programmers.co.kr/learn/courses/30/lessons/12905#

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> board)
{
    int n = board.size();
    int m = board[0].size();
    
    vector<vector<int>> dp(n+1);
    for (int i=0; i<n+1; i++) {
        dp[i].resize(m+1);
    }
    
    for (int x=0; x<n; x++) {
        for (int y=0; y<m; y++) {
            if (board[x][y] == 1) {
                if (dp[x][y] == dp[x][y+1] && dp[x][y] == dp[x+1][y]) {
                    dp[x+1][y+1] = dp[x][y] + 1;
                } else {
                    dp[x+1][y+1] = min({ dp[x][y], dp[x][y+1], dp[x+1][y] }) + 1;
                    
                    // 처음 시도
                    // (아래처럼 하면 [[1, 1, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0]] 에서 반례)
                    // dp[x+1][y+1] = max({ dp[x][y], dp[x][y+1], dp[x+1][y] });
                }
            }
        }
    }
    
    int maxSize = 0;
    for (vector<int>& v: dp) {
        for (int e: v) {
            maxSize = max(maxSize, e);
        }
    }

    return maxSize * maxSize;
}
