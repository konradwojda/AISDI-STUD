#include "kmp.h"
#include <iostream>

int main()
{
	std::string pattern = "ABACABAB";
	std::vector<int> kmp = kmp_match_table(pattern);
	for (auto e : kmp)
	{
		std::cout << e << std::endl;
	}
	return 0;
}