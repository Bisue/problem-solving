// 동전 금고
// https://study.helloalgo.co.kr/study/1019/room/598/6561

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> board;
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

bool isPossible(int n, int m, int ladder)
{
    queue<pair<int, int>> q;
    bool visited[1001][1001];
    for (int x = 0; x < 1001; x++)
    {
        for (int y = 0; y < 1001; y++)
        {
            visited[x][y] = false;
        }
    }

    q.push({0, 0});
    visited[0][0] = true;
    while (!q.empty())
    {
        pair<int, int> cur = q.front();
        q.pop();
        int cx = cur.first, cy = cur.second;
        if (cx == n - 1 && cy == m - 1)
        {
            return true;
        }

        for (int di = 0; di < 4; di++)
        {
            int nx = cx + dx[di], ny = cy + dy[di];
            if (0 <= nx && nx < n && 0 <= ny && ny < m && board[cx][cy] + ladder >= board[nx][ny] && !visited[nx][ny])
            {
                q.push({nx, ny});
                visited[nx][ny] = true;
            }
        }
    }

    return false;
}

int main()
{
    int N, M, temp;
    cin >> N >> M;
    board.resize(N);
    for (int i = 0; i < N; i++)
    {
        board[i].resize(M);
        for (int j = 0; j < M; j++)
        {
            cin >> temp;
            board[i][j] = temp;
        }
    }

    int start = 0, end = 1000000000;
    int answer = -1;
    while (start <= end)
    {
        int mid = (start + end) / 2;

        if (isPossible(N, M, mid))
        {
            answer = mid;
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }

    cout << answer << '\n';

    return 0;
}
