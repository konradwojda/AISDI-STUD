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
    heap.add_elem(unsigned int(0), size_t(2));
    //for (int i = 0; i < 10; i++)
    //{
    //    heap.add_elem(i, i*3);
    //}
    return 0;
}