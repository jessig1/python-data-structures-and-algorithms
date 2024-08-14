#array implementation
stack = []

stack.append(3)
stack.append(4)
stack.pop()
stack.append(5)
stack.append(6)
stack.pop()
stack.pop()

print(stack)

#single linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
        self._max_allowed_size = 10
    
    def push(self, value):
        if self._max_allowed_size == self._size:
            raise Exception("stack size exceeded")
        new_element = Node(value)
        new_element.next = self._top
        self._top = new_element
        self._size += 1
        return self
    def pop(self):
        if not self._size:
            raise Exception("stack is empty")
        former_top = self._top
        self._top = former_top.next
        former_top.next = None
        self._size -= 1
        return former_top.value
    def peek(self):
        return self._top.value if self._top else None
    def clear(Self):
        Self._top = None
        Self._size = 0
        return Self
    def __len__ (self):
        return self._size
    
my_stack = Stack()

my_stack.push('google')
my_stack.push('amazon')
my_stack.pop()
my_stack.pop()

print(my_stack.peek())
print(len(my_stack))