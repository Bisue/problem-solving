// 소방서
// https://study.helloalgo.co.kr/study/1019/room/596/6542

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K;

    vector<int> roads[2001];
    for (int i = 0; i < M; i++)
    {
        int s, e;
        cin >> s >> e;

        roads[s].push_back(e);
        roads[e].push_back(s);
    }

    queue<int> q;
    int dists[2001];
    for (int i = 0; i <= N; i++)
    {
        dists[i] = -1;
    }

    for (int i = 0; i < K; i++)
    {
        int station;
        cin >> station;

        q.push(station);
        dists[station] = 0;
    }

    while (!q.empty())
    {
        int cv = q.front();
        q.pop();

        for (int nv : roads[cv])
        {
            if (dists[nv] < 0)
            {
                q.push(nv);
                dists[nv] = dists[cv] + 1;
            }
        }
    }

    for (int i = 1; i <= N; i++)
    {
        cout << dists[i] << '\n';
    }
}
