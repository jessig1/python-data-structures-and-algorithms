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

def shell_sort(array):
    gaps = [5, 3, 1]
    for gap in gaps:
        for i in range(gap, len(array)):
            j = i - gap
            while array[j + gap] < array[j] and j >= 0:
                array[j], array[j + gap] = array[j+gap], array[j]
                j -= gap
    return array
