#include "kmp.h"
#include <iostream>

int main()
{
	std::string pattern = "";
	std::string text = "ABC ABC";
	std::vector<int> result = kmp_find(pattern, text);
	for (auto e : result)
	{
		std::cout << e << std::endl;
	}
	return 0;
}