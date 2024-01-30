// 조건 수열
// https://study.helloalgo.co.kr/study/1019/room/592/6475

#include <iostream>
#include <vector>
#define N_MAX 16
#define K_MAX 51
using namespace std;

vector<int> diffConds[N_MAX];
vector<int> sameConds[N_MAX];
char perms[N_MAX];
int answer = 0;

void initVars()
{
    for (int i = 0; i < N_MAX; i++)
    {
        diffConds[i] = vector<int>();
        sameConds[i] = vector<int>();
    }
}

void printPerms()
{
    for (char e : perms)
    {
        cout << e;
    }
    cout << '\n';
}

void dfs(int N, int pos)
{
    if (pos == N)
    {
        answer++;
        return;
    }

    for (char ch : {'A', 'B', 'C'})
    {
        perms[pos] = ch;
        bool impossible = false;
        for (int prev : sameConds[pos])
        {
            if (perms[prev] != perms[pos])
            {
                impossible = true;
                break;
            }
        }
        if (impossible)
            continue;

        for (int prev : diffConds[pos])
        {
            if (perms[prev] == perms[pos])
            {
                impossible = true;
                break;
            }
        }
        if (impossible)
            continue;

        dfs(N, pos + 1);
    }
}

int main()
{
    initVars();

    int N, K;
    cin >> N >> K;

    for (int i = 0; i < K; i++)
    {
        char type;
        int x, y;
        cin >> type >> x >> y;

        if (x > y)
        {
            int temp = x;
            x = y;
            y = temp;
        }

        if (type == 'S')
        {
            sameConds[y - 1].push_back(x - 1);
        }
        else if (type == 'D')
        {
            diffConds[y - 1].push_back(x - 1);
        }
    }

    dfs(N, 0);
    cout << answer << '\n';

    return 0;
}
