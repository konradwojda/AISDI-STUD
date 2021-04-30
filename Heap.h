#pragma once
#include <vector>
#include <iostream>
#include <algorithm>
#include <math.h> 

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
		//std::ostream& operator<<(std::ostream& os);
		void show(std::ostream& os);
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
	int depth(int first_elem, int n);
	template <typename T, size_t A> friend
		std::ostream& operator<<(std::ostream& os, Heap& heap);
};

template <typename T, size_t A>
Heap<T, A>::Heap()
{}

template <typename T, size_t A>
Heap<T, A>::Heap(const std::vector<Element>& other)
{
	heap_ = other;
	for (int i = size(heap_)-1; i >= 0; --i)
		heapify_down(i);
}

template<typename T, size_t A>
void Heap<T, A>::Element::show(std::ostream& os)
{
	os << "(" << key_ << ", " << value_ << ")";
}

//template <typename T, size_t A>
//std::ostream& Heap<T, A>::Element::operator<<(std::ostream& os)
//{
//	os << "sDF";
//	return os;
//}

//Returns index of parent of given child's id
template<typename T, size_t A>
int Heap<T, A>::parent(int i)
{
	if (i < 1)
		return 0;
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
	std::vector<unsigned int> family_key;
	family_ids.push_back(i);
	family_key.push_back(heap_[i].key_);
	for (int j = 0; j < A; j++)
	{
		int child_ = child(i, j);
		if (child_ < heap_.size())
		{
			family_ids.push_back(child_);
			family_key.push_back(heap_[child_].key_);
		}
	}
	return family_ids[std::max_element(family_key.begin(), family_key.end()) - family_key.begin()];
}

template<typename T, size_t A>
void Heap<T, A>::add_elem(unsigned int key_, T value)
{
	Element new_elem = { key_, value };
	heap_.push_back(new_elem);
	int id = heap_.size() - 1;
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
int Heap<T, A>::depth(int first_elem, int n)
{
	if (n == 1)
		return first_elem;
	return depth(first_elem, n - 1) * A + A - 1;
}

template<typename T, size_t A>
std::ostream& operator<<(std::ostream& os, Heap< T, A>& heap)
{
	std::string gap = "     ";
	int heap_size = heap.heap_.size();
	int height = (int)(ceil(log(heap_size * A - heap_size + 1) / log(A)));
	int current_height = height;
	int first_gap = heap.depth(A - 1, current_height - 1);
	int btw_gap = heap.depth(1, current_height);
	int number_of_elements = pow(A, height - current_height);
	int current_element = number_of_elements;
	for (int i = 0; i < heap_size; ++i)
	{
		if (number_of_elements == current_element)
		{
			for (int i = 0; i < first_gap; i++)
				os << gap;
		}
		heap.heap_[i].show(os);
		for (int i = 0; i < btw_gap; i++)
			os << gap;
		current_element--;
		if (current_element < 1)
		{
			os << "\n";
			current_height--;
			number_of_elements = pow(A, height - current_height);
			current_element = number_of_elements;
			if (current_height <= 1)
			{
				first_gap = 0;
				btw_gap = 0;
			}
			else
			{
				first_gap = heap.depth(A - 1, current_height - 1);
				btw_gap = heap.depth(1, current_height);
			}
		}
	}
	return os;
}
