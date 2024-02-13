// 수 정렬하기
// https://study.helloalgo.co.kr/study/1019/room/600/6576

// python 시간 초과로 cpp로 통과.

#include <iostream>
#include <vector>
using namespace std;

vector<int> heap;

int getLeftIdx(int cur)
{
    return cur * 2 + 1;
}
int getRightIdx(int cur)
{
    return cur * 2 + 2;
}
int getParentIdx(int cur)
{
    return cur % 2 == 0 ? cur / 2 - 1 : cur / 2;
}

int swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

void heapUp(int idx)
{
    int pIdx = getParentIdx(idx);
    while (pIdx >= 0)
    {
        if (heap[idx] < heap[pIdx])
        {
            swap(heap[idx], heap[pIdx]);
        }

        idx = pIdx;
        pIdx = getParentIdx(idx);
    }
}

void heapDown(int idx)
{
    while (true)
    {
        int left, right;
        left = getLeftIdx(idx);
        right = getRightIdx(idx);

        if (left < heap.size() && heap[left] < heap[idx] && (right >= heap.size() || heap[left] < heap[right]))
        {
            swap(heap[idx], heap[left]);
            idx = left;
        }
        else if (right < heap.size() && heap[right] < heap[idx] && heap[right] <= heap[left])
        {
            swap(heap[idx], heap[right]);
            idx = right;
        }
        else
        {
            break;
        }
    }
}

void add(int num)
{
    heap.push_back(num);
    heapUp(heap.size() - 1);
}

int remove()
{
    if (heap.size() == 0)
    {
        int result = heap.back();
        heap.pop_back();
        return result;
    }

    int result = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    heapDown(0);

    return result;
}

int main()
{
    int N, temp;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        add(temp);
    }

    while (heap.size() > 0)
    {
        cout << remove() << '\n';
    }

    return 0;
}
