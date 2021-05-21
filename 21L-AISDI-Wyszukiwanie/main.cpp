#include "kmp.h"
#include "naive.h"
#include <iostream>

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
	return 0;
}