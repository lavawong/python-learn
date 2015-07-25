#!/usr/bin/python2.7
"""
This is divide-conquar algorithm
Merge Sort
"""
def merge(left, right):
	i = 0
	j = 0
	ret = []
	while i<len(left) and j<len(right):
		if left[i] > right[j]:
			ret.append(left[i])
			i += 1
		else:
			ret.append(right[j])
			j += 1
	
	while i < len(left):
		ret.append(left[i])
		i += 1
	while j < len(right):
		ret.append(right[j])
		j += 1
	
	return ret
"""
divide into two sections and merge it
"""
def mergeSort(arr):
	l = len(arr)
	if l < 2:
		return arr[:]
	else:
		middle = l/2
		left = mergeSort(arr[:middle])
		right = mergeSort(arr[middle:])
		ret = merge(left, right)
	return ret

def test():
	arr = [2,234,33,45345,2342,234,564,2,45,234,45,234]
	arr = mergeSort(arr)
	print arr
	
	arr = []
	arr = mergeSort(arr)
	print arr

test()


