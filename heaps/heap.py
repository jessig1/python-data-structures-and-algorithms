# insert
class MaxBinaryHeap:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)
        self.move_up()

    def move_up(self):
        child_index = len(self.items) - 1
        while child_index > 0:
            parent_index = (child_index - 1)// 2
            if self.items[child_index] <= self.items[parent_index]:
                break
            self.swap(child_index, parent_index)
            child_index = parent_index

#remove max when moving smaller values at root always swap with smallest child
    def swap(self, index_1, index_2):
        self.items[index_1], self.items[index_2] = self.items[index_2], self.items[index_1]

    def remove_max(self):
        if not self.items:
            raise Exception("Heap is empty")
        max_elem = self.items[0]
        end_index = len(self.items) -1
        self.swap(0, end_index)
        self.items.pop()
        self.move_down()
        return max_elem

    def move_down(self):
        parent_index = 0
        child_index = 2 * parent_index + 1
        end_index = len(self.items) - 1
        while child_index <= end_index:
            if child_index < end_index and self.items[child_index] < self.items[child_index + 1]:
                child_index += 1
            if self.items[parent_index] < self.items[child_index]:
                self.swap(parent_index, child_index)
                parent_index = child_index
                child_index = 2 * parent_index +1
            else:
                break

#heapify takes random numbers and sets them up as a heap by moving from the bottom up
    def heapify(array):
        last_parent_index = len(array) // 2 - 1
        for index in range(last_parent_index, -1, -1):
            move_down(array, index, len(array) - 1)
        return array
    
    def move_down(array, start_index, end_index):
        child_index = 2 * start_index + 1
        while child_index <= end_index:
            if child_index < end_index and array[child_index] < array[child_index + 1]:
                child_index += 1
            if array[start_index] < array[child_index]:
                array[start_index], array[child_index], array[start_index]
                start_index = child_index
                child_index = 2 * start_index + 1
            else:
                break