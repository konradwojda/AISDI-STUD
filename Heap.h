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
	void heapify_up(int i);
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
	for (int i = size(heap_)-1; i >= 0; --i)
		heapify_down(i);
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
	std::vector<unsigned int> family_ids;
	std::vector<unsigned int> family_val;
	family_ids.push_back(i);
	family_val.push_back(heap_[i].value_);
	for (int j = 0; j < A; j++)
	{
		int child_ = child(i, j);
		if (child_ < heap_.size())
		{
			family_ids.push_back(child_);
			family_val.push_back(heap_[child_].value_);
		}
	}
	return family_ids[std::max_element(family_val.begin(), family_val.end()) - family_val.begin()];
}

template<typename T, size_t A>
void Heap<T, A>::add_elem(unsigned int key_, T value)
{
	Element new_elem = { key_, value };
	heap_.push_back(new_elem);
	unsigned int id = heap_.size() - 1;
	heapify_up(id);
}

template<typename T, size_t A>
Heap<T, A>::template Element Heap<T, A>::get_peak()
{
	return heap_.begin();
}

template<typename T, size_t A>
Heap<T, A>::template Element Heap<T, A>::remove_peak()
{
	Element peak = heap_.front();
	std::swap(heap_.front(), heap_.back());
	heap_.pop_back();
	heapify_down(0);
	return peak;
}

template<typename T, size_t A>
void Heap<T, A>::heapify_up(int i)
{
	int parent_id = parent(i);
	int largest = getMax(parent_id);
	if (largest != parent_id)
	{
		heapify_down(parent_id);
		if (parent_id != 0)
			heapify_up(parent_id);
	}
}

template<typename T, size_t A>
void Heap<T, A>::heapify_down(int i)
{
	int largest = getMax(i);
	if (largest != i)
	{
		std::swap(heap_[i], heap_[largest]);
		heapify_down(largest);
	}
}	

template<typename T, size_t A>
std::ostream& operator<<(std::ostream& os, const typename Heap< T, A>::Heap& heap)
{
	for (int i = 0; i < heap.heap_.size(); ++i)
	{
		os << heap.heap_[i] << " ";
	}
	return os;
}
