#include "CppUnitTest.h"
#include "../kmp.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace Tests
{
	TEST_CLASS(Tests)
	{
	public:
		
		TEST_METHOD(TestNormalCase)
		{
			std::string pattern = "ABC";
			std::string text = "ABC ABCDAB ABCDABCDABDE";
			std::vector<int> expected = { 0, 4, 11, 15 };
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyTextCase)
		{
			std::string pattern = "ABC";
			std::string text = "";
			std::vector<int> expected = {};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyPatternCase)
		{
			std::string pattern = "";
			std::string text = "ABC ABC";
			std::vector<int> expected = {0,1,2,3,4,5,6};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEmptyBothCase)
		{
			std::string pattern = "";
			std::string text = "";
			std::vector<int> expected = {};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestEqualStringsCase)
		{
			std::string pattern = "ABC";
			std::string text = "ABC";
			std::vector<int> expected = {0};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestPatternLongerCase)
		{
			std::string pattern = "ABC ABCDAB ABCDABCDABDE";
			std::string text = "ABC";
			std::vector<int> expected = {};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
		TEST_METHOD(TestNoMatchCase)
		{
			std::string pattern = "asjnsdfjbndslkfgbsl";
			std::string text = "ABC";
			std::vector<int> expected = {};
			std::vector<int> result = kmp_find(pattern, text);
			Assert::IsTrue(expected == result);
		}
	};
}
