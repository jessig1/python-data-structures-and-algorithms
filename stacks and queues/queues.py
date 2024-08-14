class Queue:
    def __init__(self):
        self.head = None
        self._size = 0
        self.tail = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self._size:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail= new_node
        self._size += 1
        return self
    def dequeue(self):
        if not self._size:
            raise Exception("empty queue")
        former_tail = self.tail
        if self._size == 1:
            self.head = self.tail = None
        else:
            self.head = former_tail.previous
            former_tail.previous - None
        self.tail.next = None
        self._size -= 1
        return former_tail.value
    
    def peek(self):
        return self._head.value if self._head else None
    def clear(Self):
        Self.head = None
        Self.tail = None
        Self._size = 0
        return Self
    
# deques are a stack managment library in python that has methods that do most of the logic above
    