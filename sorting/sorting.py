#insertion array = compares items in array item by item. 
# time best: O(n) *everything in order average: O(n2) *reversed worst: O(n2) random
#  space: O(1)
# good for small arrays
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j], array[j -1]
    return array

#selection array = scans array then puts smalles value all the way to the left, 
# then  moves to second item in array and scans everythign to the right, moves next smallest number to the left
# time O(n2) space: O(1)
def selection_sort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i+1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array

#Bubble Sort = compares first index and last index, moves smallest item left
# time: best = O(n) worst = O(n2) space = O(1)
#very inefficent
def bubble_sort(array):
    for i in range(len(array) - 1):
        #flag variable, helps optimize to check which values have swapped to stop extra processing
        has_swapped = False
        for j in range(len(array) - 1, i, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                has_swapped = True
            if not has_swapped:
                break
    return array

#shell sort = compares items in arrays with a gap between indecies does an initial bulk sort then smaller sorts to minimize swaps
# 2n + 1 is good sequence for gaps
#space = O(1) time = many variables
def shell_sort(array):
    gaps = [5, 3, 1]
    for gap in gaps:
        for i in range(gap, len(array)):
            j = i - gap
            while array[j + gap] < array[j] and j >= 0:
                array[j], array[j + gap] = array[j+gap], array[j]
                j -= gap
    return array

#heap sort = better on large arrays turns array to heap, swaps largest and smallest value
# creates new heap minus the largest index, repeats 

def heap_sort(array):
    heapify(array)
    for end_index in range(len(array) - 1, 0, -1):
        array[0], array[end_index] = array[end_index], array[0]
        move_down(array, 0, end_index -1 )
    return array

# merge sort = splits arrays in half to smaller arrays then in half again until they are\
# invidivual pieces then adds them back together in order
# relies on recursion to split 2 sorted lists and put them in order
# time: O(nlogn) space: O(n)

def merge_sort(array):
    if len(array) < 2:
        return array
    first_half = merge_sort(array[:len(array) // 2])
    second_half = merge_sort(array[len(array) // 2:])
    return merge(first_half, second_half)

def merge(first_half, second_half):
    result = []
    i = j = 0 
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            result.append(first_half[i])
            i += 1
        else:
            result.append(second_half[j])
            j += 1
    while i < len(first_half):
        result.append(second_half[i])
        i += 1
    while j < len(second_half):
        result.append(second_half[j])
        j += 1
    return result

# quick sort = splits arrays then sorts in place  
def quick_sort(array):
    if len(array) < 2:
        return array
    return partition(array, 0, len(array) - 1 )

def partition(array, start, end):
    pivot = end
    boundary = start
    for i in range(start, end):
        if array[i] <= array[pivot]:
            array[boundary, array[i]] = array[i], array[boundary]
            boundary += 1
        array[boundary], array[end] = array[end], array[boundary]
        partition(array, start, boundary - 1)
        partition(array, boundary + 1, end)
        return array
#radix sort

import math

def radix_sort(array):
    max_digits = get_max_number_of_digits(array)
    for i in range(max_digits + 1):
        buckets = [[] for _ in range(10)]
        for num in array:
            digit = get_digit_at_position(num, position=i)
            buckets[digit].append(num)
        array = flatten(buckets)
    return array

def get_max_number_of_digits(array):
    return max(int(math.log10(abs(num))) + 1 if num != 0 else 1 for num in array)

def get_digit_at_position(number, position):
    return (abs(number) // 10 ** position) % 10

def flatten(array):
    return [num for inner in array for num in innter]