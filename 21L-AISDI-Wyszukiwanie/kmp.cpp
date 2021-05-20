#include "kmp.h"

std::vector<int> kmp_match_table(std::string const& pattern)
{
	std::vector<int> kmp_table;
	kmp_table.push_back(0);
	int prefix_len = 0;
	int pattern_id = 1;

	while (pattern_id < pattern.length())
	{
		if (pattern[prefix_len] == pattern[pattern_id])
			{
				prefix_len++;
			}
		else if (prefix_len > 0)
		{
			prefix_len = kmp_table[prefix_len - 1];
			continue;
		}
		kmp_table.push_back(prefix_len);
		pattern_id++;
	}
	return kmp_table;
}