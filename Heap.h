#pragma once
#include <vector>
#include <iostream>
#include <algorithm>

template <typename T, size_t A>
class Heap
{
public:
	Heap();
	//Heap(const std::vector<Element>& other);
	struct Element
	{
		unsigned int key_;
		T value_;
		friend
			std::ostream& operator<<(std::ostream& os, const Element& elem);
	};
	Heap(const std::vector<Element>& other);
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

template <typename T, size_t A>
Heap<T, A>::Heap()
{}

template<typename T, size_t A>
Heap<T, A>::Heap(const std::vector<Element>& other)
{
	heap_ = other;
}

template<typename T, size_t A>
std::ostream& operator<<(std::ostream& os, const typename Heap< T, A>::Element& elem)
{
	os << "(" << elem.key_ << ", " << elem.value_ << ")";
	return os;
}

//Returns index of parent of given child's id
template<typename T, size_t A>
int Heap<T, A>::parent(const int i)
{
	return (i - 1) / A;
}

//Returns index of <0, A) child of given parent's id 
template<typename T, size_t A>
int Heap<T, A>::child(const int i, const int child_id)
{
	return (i * A) + child_id + 1;
}

//Returns index maximum value of children and parent of given parent's id
template<typename T, size_t A>
int Heap<T, A>::getMax(const int i)
{
	std::vector<int> family_ids;
	std::vector<int> family_val;
	family_ids.push_back(i);
	family_val.push_back(heap_[i]);
	for (int j = 0; j < A; j++)
	{
		int child = child(i, j);
		if (child < heap_.size)
		{
			family_ids.push_back(child);
			family_val.push_back(heap_[child]);
		}
	}
	return family_ids[std::max_element(family_val.begin(), family_val.end()) - family_val.begin()];
}