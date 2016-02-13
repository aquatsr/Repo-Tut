# Date: March 3, 2014
# FIle: bubblesort.py
# Purpose: <classified>

import random

def run(input_list):
	needed_sort = True
	while needed_sort:
		needed_sort = False
		for item in range(1, len(input_list)):
			if input_list[item - 1] > input_list[item]:
				temp = input_list[item - 1]
				input_list[item - 1] = input_list[item]
				input_list[item] = temp
				needed_sort = True
	return input_list

if __name__ == '__main__':
	sample = [x for x in range(0,11)]
	random.shuffle(sample)
	print "Original: ", sample
	print "Sorted: ", run(sample)
