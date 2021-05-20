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

/*
* Uses KMP algorithm to find pattern in text.
* Return vector with ids where pattern has been found in text
* If length of text is 0, returns vector with -1 as first element.
* If length of pattern is 0, returns vector with numbers from 0 to text length
*/

std::vector<int> kmp_find(std::string const& pattern, std::string const& text)
{
	std::vector<int> kmp_table = kmp_match_table(pattern);
	std::vector<int> result;
	int matched_numbers = 0;
	int text_id = 0;
	if (pattern.length() == 0)
	{
		for (int i = 0; i < text.length(); i++)
		{
			result.push_back(i);
		}
		return result;
	}
	if (text.length() == 0)
	{
		result.push_back(-1);
		return result;
	}
	while (text_id < text.length())
	{
		if (text[text_id] == pattern[matched_numbers])
		{
			matched_numbers++;
			text_id++;
			if (matched_numbers == pattern.length())
			{
				result.push_back(text_id - pattern.length());
				matched_numbers = kmp_table[kmp_table.size() - 1];
			}
		}
		else if (matched_numbers > 0)
		{
			matched_numbers = kmp_table[matched_numbers - 1];
		}
		else
		{
			text_id++;
		}
	}
	return result;
}	

