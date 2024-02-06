// 서브트리 노드 수 구하기
// https://study.helloalgo.co.kr/study/1019/room/597/6550

#include <iostream>
#include <vector>
using namespace std;

vector<int> tree[100001];
int cache[100001] = {
    0,
};
bool visited[100001] = {
    false,
};

int countSubtreeNodes(int cv)
{
    if (cache[cv] > 0)
    {
        return cache[cv];
    }

    visited[cv] = true;

    int nodes = 1;
    for (int nv : tree[cv])
    {
        if (!visited[nv])
        {
            nodes += countSubtreeNodes(nv);
        }
    }

    cache[cv] = nodes;
    return nodes;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, R, Q;
    cin >> N >> R >> Q;

    for (int i = 0; i < N - 1; i++)
    {
        int u, v;
        cin >> u >> v;

        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    visited[R] = true;
    countSubtreeNodes(R);

    for (int i = 0; i < Q; i++)
    {
        int u;
        cin >> u;

        visited[u] = true;
        cout << countSubtreeNodes(u) << '\n';
    }
}
