#include "kmp.h"
#include "naive.h"
#include <iostream>
#include <chrono>

int main()
{
	std::string pattern = "";
	std::string text = "ABC ABC";
	std::vector<int> kmp_result = kmp_find(pattern, text);
	std::vector<int> naive_result = naive_find(pattern, text);
	std::cout << "KMP:\n";
	for (auto e : kmp_result)
	{
		std::cout << e << std::endl;
	}
	std::cout << "NAIVE:\n";
	for (auto e : naive_result)
	{
		std::cout << e << std::endl;
	}

	auto t1 = std::chrono::high_resolution_clock::now();
	//FIND FUNCTION
	auto t2 = std::chrono::high_resolution_clock::now();

	std::chrono::duration<double, std::milli> fp_ms = t2 - t1;

	auto int_ms = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1);
	std::chrono::duration<long, std::micro> int_usec = int_ms;

	std::cout << "Time" << fp_ms.count() << " ms\n";

	return 0;
}