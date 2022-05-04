#include "Heap.h"
#include <iostream>
#include <chrono>

using namespace std;

int main()
{
    Heap<int, 2> heap = Heap<int, 2>();
    for (int i = 0; i < 10; ++i)
    {
        heap.add_elem(i, 0);
    }
    //auto t1 = std::chrono::high_resolution_clock::now();
    //heap.remove_peak();
    //auto t2 = std::chrono::high_resolution_clock::now();

    //std::chrono::duration<double, std::milli> fp_ms = t2 - t1;

    //auto int_ms = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1);
    //std::chrono::duration<long, std::micro> int_usec = int_ms;

    //std::cout << "Time" << fp_ms.count() << " ms\n";
    std::cout << heap;
    return 0;
}