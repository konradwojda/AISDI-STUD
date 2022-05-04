#include "rabin_karp.h"

std::vector<int> rabin_karp_find(std::string const& pattern, std::string const& txt, int prime_number) {
	int txt_len = txt.length();
	int pat_len = pattern.length();
    if (pat_len > txt_len)
        return {};
    int pat_hash_value{ 0 };
    int txt_hash_value{ 0 };
    int control_value = 1;
    int maxchar = 512;
    std::vector<int> result;

    if (pattern.length() == 0)
    {
        for (int i = 0; i <= txt_len; i++)
        {
            result.push_back(i);
        }
        return result;
    }
    if (txt_len == 0)
    {
        return result;
    }

    for (int i = 0; i < pat_len - 1; i++)
        control_value = (control_value * maxchar) % prime_number;

    for (int i = 0; i < pat_len; i++)
    {
        pat_hash_value = (maxchar * pat_hash_value + pattern[i]) % prime_number;
        txt_hash_value = (maxchar * txt_hash_value + txt[i]) % prime_number;
    }

    for (int i = 0; i <= txt_len - pat_len; i++)
    {
        if (pat_hash_value == txt_hash_value)
        {
            int j;
            for (j = 0; j < pat_len; j++)
            {
                if (txt[i + j] != pattern[j])
                    break;
            }
            if (j == pat_len)
                result.push_back(i);
        }

        if (i == txt_len - pat_len)
            break;

        txt_hash_value = (maxchar * (txt_hash_value - txt[i] * control_value) + txt[i + pat_len]) % prime_number;

        if (txt_hash_value < 0)
            txt_hash_value = (txt_hash_value + prime_number);
    }
    return result;
}
