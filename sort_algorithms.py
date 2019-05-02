import numpy as np
import datetime

def quick_sort(sorting_list):
	if len(sorting_list) == 0:
		return sorting_list
	less = []
	more = []
	middle = []
	middle_val = sorting_list[len(sorting_list)//2]
	for i in sorting_list:
		if i < middle_val:
			less.append(i)
		if i == middle_val:
			middle.append(i)
		if i > middle_val:
			more.append(i)
	return quick_sort(less) + middle + quick_sort(more)
	
def insertion_sort(list4sort):
	i = 1
	while i < len(list4sort):
		cur_key = list4sort[i]
		j = i - 1
		while (j>=0 and list4sort[j] > list4sort[j+1]):
			list4sort[j+1]=list4sort[j]
			j = j - 1
			list4sort[j+1] = cur_key
		i = i + 1
	return list4sort
def merge (left, right):
	result = []
	left_cur = 0
	right_cur = 0
	while left_cur < len(left) or right_cur < len(right):
		if (right_cur == len(right)):
			result.append(left[left_cur])
			left_cur = left_cur + 1
			continue
		if (left_cur == len(left)):
			result.append(right[right_cur])
			right_cur = right_cur + 1
			continue
		if (left[left_cur] < right[right_cur]):
			result.append(left[left_cur])
			left_cur = left_cur + 1
		else:
			result.append(right[right_cur])
			right_cur = right_cur + 1
	return result
def merge_sort(list4sort):
	if len(list4sort)<=1:
		return list4sort
	left = merge_sort(list4sort[:len(list4sort)//2])
	right = merge_sort(list4sort[len(list4sort)//2:])
	return merge(left, right)

def testSorted(list4sort):
	i = 0
	while i < len(list4sort) - 1:
		if list4sort[i] >= list4sort[i + 1]:
			return 1
		i = i +1
	return 0

def evaluateTime(func, N=20, Size = 100):
	times = []
	for i in range(0,N):
		to_sort = np.random.random_sample((Size,))
		list4sort  = [i for i in to_sort]
		start = datetime.datetime.now()
		list4sort = func(list4sort)
		end = datetime.datetime.now()
		if testSorted(list4sort) > 0:
			print ("sorting failed")
		worktime = (end-start)/datetime.timedelta(microseconds=1)
		times.append(worktime)
	average_time = sum(times)/len(times)
	print(func.__name__,average_time)



if __name__ == "__main__":
	
	
	evaluateTime(merge_sort,10,10000)
	evaluateTime(insertion_sort,10,10000)
	evaluateTime(quick_sort,10,10000)
	

	





