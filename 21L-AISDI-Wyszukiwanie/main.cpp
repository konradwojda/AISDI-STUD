#include "kmp.h"
#include <iostream>

int main()
{
	std::string pattern = "adasdad";
	std::string text = "f";
	std::vector<int> result = kmp_find(pattern, text);
	for (auto e : result)
	{
		std::cout << e << std::endl;
	}
	return 0;
}