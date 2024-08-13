class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    # append = add new elements to tail of list
    # time: O(1) space: O(1)
    def append(self, value):
        new_node = Node(value)
        #checks if length is empty
        if not self._length:
            #assigns new_node to head and tail
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        return self
    
my_list = SinglyLinkedList()
my_list.append(3)
my_list.append(5)

print(my_list)
print(my_list.head.value)
print(my_list.tail.value)
print(my_list._length)

#prepend = add element at beginning (head) of list
# time: O(1) space O(1)
def prepend(self, value):
    new_node = Node(value)
    if not self._length:
        self.head = self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node
    self._length += 1
    return self

#remove head (pop left) = remove from left of list

def pop_left(self):
    if not self._length:
        raise Exception("empty list")
    former_head = self.head
    self.head = former_head.next
    former_head.next = None
    self._length -= 1
    if not self._length:
        self.tail = None
    return former_head.value

#remove tail (pop right) = remove from right of list
#time = O(n) due to nested loop space = O(1)
def pop_right(self):
    if not self._length:
        raise Exception("empty list")
    tail_value = self.tail.value
    if not self._length:
        self.head = self.tail = None
    else:
        temp_node = self.head
        while temp_node.next is not self.tail:
            temp_node = temp_node.next
        self.tail = temp_node
        self.tail.next = None
    self._length -= 1
    return tail_value

#remove defined value time = O(n) space = O(1)
def remove(self, value):
    if not self._length:
        raise Exception("empty list")
    if self.head.value == value:
        return self.pop_left()
    previous_node = self.head.next
    current_node = self.head.next
    while current_node is not None and current_node.value != value:
        previous_node = current_node = current_node
        current_node = current_node.next
    if current_node is None:
        raise ValueError("Item not on list")
    if current_node.Next is None:
        self.tail = previous_node
    previous_node.next = current_node.next
    current_node.next = None
    self._length -= 1
    return current_node.value
# time =  O(n) space = O(1)
def reverse(self):
    if self._length < 2:
        return self
    left_node = None
    middle_node = self.head
    while middle_node is not None:
        right_node = middle_node.next
        middle_node.next = left_node
        left_node = middle_node
        middle_node = right_node
    self.head, self.tail = self.tail, self.head
    return self