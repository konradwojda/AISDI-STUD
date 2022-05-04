#include "kmp.h"
#include "naive.h"
#include "rabin_karp.h"
#include <iostream>
#include <chrono>

std::string generate_alphabet(int number)
{
	const int MAX = 5;
	std::string result = "";
	char alphabet[MAX] = { 'a', 'b', 'c'};

	for (int i = 0; i < number; i++)
		result = result + alphabet[rand() % MAX];
	return result;
}


int main()
{
	srand(time(NULL));
	//std::vector<int> kmp_result = kmp_find(pattern, text);
	//std::vector<int> naive_result = naive_find(pattern, text);
	//std::vector<int> rb_result = rabin_karp_find(pattern, text, 5);

	std::string alphabet = "";
	std::string pattern = "";
	std::chrono::steady_clock::time_point t1, t2;
	std::chrono::microseconds int_ms;
	std::chrono::duration<double, std::milli> fp_ms;
	alphabet = generate_alphabet(500000);
	for (int i = 1; i <= 10; i++)
	{
		pattern = generate_alphabet(i * 1000);

		t1 = std::chrono::high_resolution_clock::now();
		std::vector<int> naive_result = naive_find(pattern, alphabet);
		t2 = std::chrono::high_resolution_clock::now();

		fp_ms = t2 - t1;

		std::cout <<fp_ms.count() << ", ";

		t1 = std::chrono::high_resolution_clock::now();
		std::vector<int> sd_result = kmp_find(pattern, alphabet);
		t2 = std::chrono::high_resolution_clock::now();

		fp_ms = t2 - t1;

		std::cout << fp_ms.count() << ", ";

		t1 = std::chrono::high_resolution_clock::now();
		std::vector<int> asde_result = rabin_karp_find(pattern, alphabet, 5);
		t2 = std::chrono::high_resolution_clock::now();

		fp_ms = t2 - t1;

		std::cout << fp_ms.count() << "\n";
	}

	return 0;
}