#include "Heap.h"
#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

int main()
{
    high_resolution_clock::time_point t1 = high_resolution_clock::now();
    //your code here
    high_resolution_clock::time_point t2 = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>(t2 - t1).count();

    cout << duration;

    Heap<int, 2> heap = Heap<int, 2>();
    heap.add_elem(0, 0);
    heap.add_elem(11, 0);
    heap.add_elem(22, 0);
    heap.add_elem(33, 0);
    heap.add_elem(44, 0);
    heap.add_elem(55, 0);
    heap.add_elem(66, 0);
    heap.add_elem(30, 0);

    for (int i = 0; i < heap.heap_.size(); i++)
    {
        std::cout << heap.heap_[i];
    }
    return 0;
}