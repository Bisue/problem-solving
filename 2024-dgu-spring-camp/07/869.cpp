// 보물섬(KOI지역2005_초등부_3)
// https://study.helloalgo.co.kr/study/1019/room/594/6489

#include <iostream>
#include <queue>
#include <vector>
#include <string>
#define MAX_SIZE 51
using namespace std;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int N, M;
char board[MAX_SIZE][MAX_SIZE];

int bfs(int sx, int sy, int &rx, int &ry)
{
	queue<pair<int, int>> q;
	int dists[MAX_SIZE][MAX_SIZE];
	for (int x = 0; x < N; x++)
	{
		for (int y = 0; y < M; y++)
		{
			dists[x][y] = -1;
		}
	}

	int resultMax = 0, resultX = sx, resultY = sy;

	q.push({sx, sy});
	dists[sx][sy] = 0;
	while (!q.empty())
	{
		pair<int, int> cur = q.front();
		q.pop();
		int cx = cur.first, cy = cur.second;

		if (dists[cx][cy] >= resultMax)
		{
			resultMax = dists[cx][cy];
			resultX = cx;
			resultY = cy;
		}

		for (int d = 0; d < 4; d++)
		{
			int nx = cx + dx[d], ny = cy + dy[d];
			if (0 <= nx && nx < N && 0 <= ny && ny < M && board[nx][ny] == 'L' && dists[nx][ny] < 0)
			{
				q.push({nx, ny});
				dists[nx][ny] = dists[cx][cy] + 1;
			}
		}
	}

	rx = resultX;
	ry = resultY;
	return resultMax;
}

int main()
{
	// ios_base::sync_with_stdio(false);
	// cin.tie(NULL); cout.tie(NULL);

	scanf("%d %d", &N, &M);
	getchar(); //
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			scanf("%1c", &board[i][j]);
		}
		getchar(); //
	}

	int answer = -1;
	for (int x = 0; x < N; x++)
	{
		for (int y = 0; y < M; y++)
		{
			if (board[x][y] == 'L')
			{
				int rd, rx, ry;
				rd = bfs(x, y, rx, ry);
				if (rd > answer)
				{
					answer = rd;
				}
			}
		}
	}

	cout << answer << '\n';

	return 0;
}
