#pragma once
#include <vector>
#include <string>

std::vector<int> kmp_match_table(std::string const& pattern);

std::vector<int> kmp_find(std::string const& pattern, std::string const& text);