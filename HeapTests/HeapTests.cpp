#include "CppUnitTest.h"
#include "..\Heap.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace HeapTests
{
	TEST_CLASS(HeapTests)
	{
	public:
		TEST_METHOD(AddElem2)
		{
			Heap<int, 2> heap = Heap<int, 2>();
			heap.add_elem(1, 0);
			Assert::AreEqual(heap.heap_[0].key_, (unsigned int)1);
		}
		TEST_METHOD(AddTwoElems2)
		{
			Heap<int, 2> heap = Heap<int, 2>();
			heap.add_elem(1, 0);
			heap.add_elem(2, 0);
			Assert::AreEqual(heap.heap_[0].key_, (unsigned int)2);
		}
		TEST_METHOD(RemovePick2)
		{
			Heap<int, 2> heap = Heap<int, 2>();
			heap.add_elem(1, 0);
			heap.add_elem(2, 0);
			heap.remove_peak();
			Assert::AreEqual(heap.heap_[0].key_, (unsigned int)1);
		}
		TEST_METHOD(getMax2)
		{
			Heap<int, 2> heap = Heap<int, 2>();
			heap.add_elem(1, 0);
			heap.add_elem(2, 0);
			heap.add_elem(3, 0);
			heap.add_elem(4, 0);
			auto value = heap.getMax(3);
			Assert::AreEqual(value, 3);
		}
		TEST_METHOD(getpeak2)
		{
			Heap<int, 2> heap = Heap<int, 2>();
			heap.add_elem(1, 0);
			heap.add_elem(2, 0);
			heap.add_elem(3, 0);
			heap.add_elem(4, 0);
			auto value = heap.get_peak().key_;
			Assert::AreEqual(value, (unsigned int)4);
		}
		TEST_METHOD(AddElem5)
		{
			Heap<int, 5> heap = Heap<int, 5>();
			heap.add_elem(1, 0);
			Assert::AreEqual(heap.heap_[0].key_, (unsigned int)1);
		}
		TEST_METHOD(AddTwoElems5)
		{
			Heap<int, 5> heap = Heap<int, 5>();
			heap.add_elem(1, 0);
			heap.add_elem(2, 0);
			Assert::AreEqual(heap.heap_[0].key_, (unsigned int)2);
		}
		TEST_METHOD(RemovePick5)
		{
			Heap<int, 5> heap = Heap<int, 5>();
			heap.add_elem(1, 0);
			heap.add_elem(2, 0);
			heap.remove_peak();
			Assert::AreEqual(heap.heap_[0].key_, (unsigned int)1);
		}
		TEST_METHOD(getMax5)
		{
			Heap<int, 5> heap = Heap<int, 5>();
			heap.add_elem(1, 0);
			heap.add_elem(2, 0);
			auto value = heap.getMax(1);
			Assert::AreEqual(value, 1);
		}
		TEST_METHOD(getpeak5)
		{
			Heap<int, 2> heap = Heap<int, 2>();
			heap.add_elem(1, 0);
			heap.add_elem(2, 0);
			heap.add_elem(3, 0);
			heap.add_elem(4, 0);
			auto value = heap.get_peak().key_;
			Assert::AreEqual(value, (unsigned int)4);
		}
	};
}