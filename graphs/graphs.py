#adding vertices and edges

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex in self.adjacency_list:
            raise Exception("vertex already in graph")
        self.adjacency_list[vertex] = []
        return self
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise Exception("Invalid vertices")
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        return self
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise Exception("Invalid vertices")
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)
        return self
    
    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            raise Exception("vertex not in graph")
        for neighbor in self.adjacency_list[vertex]:
            self.adjacency_list[neighbor].remove(vertex)
        self.adjacency_list.pop(vertex)
        return self
    
#breadth first traversal
def breadth_first_traversal(self, start):
    if start not in self.adjaceny_list:
        raise Exception("Vertex not in graph")
    queue = deque()
    queue.append(start)
    visited = []
    explored = {vertex: False for vertex in self.adjacency_list}
    explored[start] = True
    while queue:
        current = queue.popleft()
        visited.append(current)
        for adjacent in self.adjacency_list[current]:
            if not explored[adjacent]:
                queue.append(adjacent)
                explored[adjacent] = True
    return visited

#breadth first iterative
def dft_iterative(self, start):
    if start not in self.adjacency_list:
        raise Exception("Vertex not in graph")
    stack = [start]
    visited = []
    explored = {vertex: False for vertex in self.adjacency_list}
    explored[start] = True
    while stack:
        current = stack.pop()
        visited.append(current)
        for adjacent in self.adjacency_list[current]:
            if not explored[adjacent]:
                stack.append(adjacent)
                explored[adjacent] = True
    return visited

#depth first traversal recursive
def dft_recursive(self,start):
    if start not in self.adjacency_list:
        raise Exception("Vertext not in graph")
    visited = []
    explored = {vertex: False for vertex in self.adjacency_list}

    def _traverse(current):
        visited.append(current)
        explored[current] = True
        for adjacent in self.adjacency_list[current]:
            if not explored[adjacent]:
                _traverse(adjacent)
        return
    _traverse(start)
    return visited
