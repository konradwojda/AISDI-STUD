#pragma once
#include <vector>
#include <iostream>

template <typename T, size_t A>
class Heap
{
public:
	Heap();
	Heap(const std::vector<Element>& other);
	struct Element
	{
		unsigned int key_;
		T value_;
		friend
			std::ostream& operator<<(std::ostream& os, const Element& elem);
	};
	std::vector<Element> heap_;
	int parent(const int i);
	int child(const int i, const int child_id);
	int getMax(const int i);
	void add_elem(unsigned int key_, T value);
	Element get_peak();
	Element remove_peak();
	//void heapify_up(int i);
	void heapify_down(int i);
	friend
		std::ostream& operator<<(std::ostream& os, const Heap& heap);
};