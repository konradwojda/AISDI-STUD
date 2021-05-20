#include "kmp.h"
#include <iostream>

int main()
{
	std::string pattern = "ABC";
	std::string text = "ABC ABCDAB ABCDABCDABDE";
	std::vector<int> result = kmp_find(pattern, text);
	for (auto e : result)
	{
		std::cout << e << std::endl;
	}
	return 0;
}