#include "naive.h"

std::vector<int> naive_find(std::string const& pattern, std::string const& text)
{
    int matched_numbers = pattern.length();
    int text_id = text.length();
    std::vector<int> result;

    int i, j;
    for (i = 0; i <= text_id - matched_numbers; ++i) {
        for (j = 0; j < matched_numbers; ++j)
            if (text[i + j] != pattern[j])
                break;
        if (j == matched_numbers)
            result.push_back(i);
    }
    return result;
}