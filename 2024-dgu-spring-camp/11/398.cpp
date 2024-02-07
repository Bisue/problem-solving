// 수 찾기
// https://study.helloalgo.co.kr/study/1019/room/598/6553/source/828365/

#include <iostream>
#include <vector>
using namespace std;

vector<int> nums, targets;

bool findNum(int n, int target)
{
    int start = 0, end = n - 1;
    while (start <= end)
    {
        int mid = (start + end) / 2;

        if (nums[mid] == target)
        {
            return true;
        }
        else if (nums[mid] > target)
        {
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }
    return false;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    int temp;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        nums.push_back(temp);
    }
    for (int i = 0; i < M; i++)
    {
        cin >> temp;
        targets.push_back(temp);
    }

    for (int target : targets)
    {
        if (findNum(N, target))
        {
            cout << "1\n";
        }
        else
        {
            cout << "0\n";
        }
    }
}
