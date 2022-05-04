#include "CppUnitTest.h"
#include "../kmp.h"
#include "../naive.h"
#include "../rabin_karp.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace Tests
{
	TEST_CLASS(Tests)
	{
	public:
		
		TEST_METHOD(TestNormalCaseKMP)
		{
			std::string pattern = "ABC";
			std::string text = "ABC ABCDAB ABCDABCDABDE";
			std::vector<int> expected = { 0, 4, 11, 15 };
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyTextCaseKMP)
		{
			std::string pattern = "ABC";
			std::string text = "";
			std::vector<int> expected = {};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyPatternCaseKMP)
		{
			std::string pattern = "";
			std::string text = "ABC ABC";
			std::vector<int> expected = {0,1,2,3,4,5,6,7};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyBothCaseKMP)
		{
			std::string pattern = "";
			std::string text = "";
			std::vector<int> expected = {0};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEqualStringsCaseKMP)
		{
			std::string pattern = "ABC";
			std::string text = "ABC";
			std::vector<int> expected = {0};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestPatternLongerCaseKMP)
		{
			std::string pattern = "ABC ABCDAB ABCDABCDABDE";
			std::string text = "ABC";
			std::vector<int> expected = {};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestNoMatchCaseKMP)
		{
			std::string pattern = "asjnsdfjbndslkfgbsl";
			std::string text = "ABC";
			std::vector<int> expected = {};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestNormalCaseNaive)
		{
			std::string pattern = "ABC";
			std::string text = "ABC ABCDAB ABCDABCDABDE";
			std::vector<int> expected = { 0, 4, 11, 15 };
			std::vector<int> result = naive_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyTextCaseNaive)
		{
			std::string pattern = "ABC";
			std::string text = "";
			std::vector<int> expected = {};
			std::vector<int> result = naive_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyPatternCaseNaive)
		{
			std::string pattern = "";
			std::string text = "ABC ABC";
			std::vector<int> expected = { 0,1,2,3,4,5,6,7 };
			std::vector<int> result = naive_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyBothCaseNaive)
		{
			std::string pattern = "";
			std::string text = "";
			std::vector<int> expected = {0};
			std::vector<int> result = naive_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEqualStringsCaseNaive)
		{
			std::string pattern = "ABC";
			std::string text = "ABC";
			std::vector<int> expected = { 0 };
			std::vector<int> result = naive_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestPatternLongerCaseNaive)
		{
			std::string pattern = "ABC ABCDAB ABCDABCDABDE";
			std::string text = "ABC";
			std::vector<int> expected = {};
			std::vector<int> result = naive_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestNoMatchCaseNaive)
		{
			std::string pattern = "asjnsdfjbndslkfgbsl";
			std::string text = "ABC";
			std::vector<int> expected = {};
			std::vector<int> result = naive_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestNormalCaseRK)
		{
			std::string pattern = "ABC";
			std::string text = "ABC ABCDAB ABCDABCDABDE";
			std::vector<int> expected = { 0, 4, 11, 15 };
			std::vector<int> result = rabin_karp_find(pattern, text, 5);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyTextCaseRK)
		{
			std::string pattern = "ABC";
			std::string text = "";
			std::vector<int> expected = {};
			std::vector<int> result = rabin_karp_find(pattern, text, 5);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyPatternCaseRK)
		{
			std::string pattern = "";
			std::string text = "ABC ABC";
			std::vector<int> expected = { 0,1,2,3,4,5,6,7 };
			std::vector<int> result = rabin_karp_find(pattern, text, 5);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyBothCaseRK)
		{
			std::string pattern = "";
			std::string text = "";
			std::vector<int> expected = { 0 };
			std::vector<int> result = rabin_karp_find(pattern, text, 5);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEqualStringsCaseRK)
		{
			std::string pattern = "ABC";
			std::string text = "ABC";
			std::vector<int> expected = { 0 };
			std::vector<int> result = rabin_karp_find(pattern, text, 5);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestPatternLongerCaseRK)
		{
			std::string pattern = "ABC ABCDAB ABCDABCDABDE";
			std::string text = "ABC";
			std::vector<int> expected = {};
			std::vector<int> result = rabin_karp_find(pattern, text, 5);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestNoMatchCaseRK)
		{
			std::string pattern = "asjnsdfjbndslkfgbsl";
			std::string text = "ABC";
			std::vector<int> expected = {};
			std::vector<int> result = rabin_karp_find(pattern, text, 5);
			Assert::IsTrue(expected == result);
		}
	};
}
