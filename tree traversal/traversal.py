#breadth first travel every branch on a level then move down
#add branches from level to a queue to traverse, then process left to right

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
#time: O(n) space: O(n)
    def breadth_first_traversal(self):
        if not self.root:
            raise Exception("Tree is empty")
        queue = deque()
        queue.append(self.root)
        visited = []
        visited_node = queue.popleft()
        visited.append(visited_node.data)
        while queue:
            if visited_node.left:
                queue.append(visited_node.left)
            if visited_node.right:
                queue.append(visited_node.right)
        return visited
    
#Pre order Iterative, goes right first then goes up, keeps looking for right branches until only left right then travese left
#Add right node and child nodes to stack, then pop off
    def dft_pre_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty")
        stack = [self.root]
        visited = []
        while stack:
            visited_node = stack.pop()
            visited.append(visited_node.data)
            if visited_node.left:
                stack.append(visited_node.left)
            if visited_node.right:
                stack.append(visited_node.right)
        return visited

#pre order recursive
    def dft_pre_order_recursive(self):
        if not self.root:
            raise Exception("Tree is empty")
        visited = []

        def _traverse(node):
            while node:
                if node:
                    visited.append(node.data)
                    _traverse(node.left)
                    _traverse(node.right)
                return
        _traverse(self.root)
        return visited

#goes from smallest to largest values in tree
    def dft_in_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty")
        current_node = self.root
        stack = []
        visited = []
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                visited_node = stack.pop()
                visited.append(visited_node)
                if not visited_node.right:
                    continue
                current_node = visited_node.right
        return visited
    
    def dft_pre_order_recursive(self):
        if not self.root:
            raise Exception("Tree is empty")
        visited = []

        def _traverse(node):
            while node:
                if node:
                    _traverse(node.left)
                    visited.append(node.data)
                    _traverse(node.right)
                return
        _traverse(self.root)
        return visited
    #goes down branch until hit leaf, then return left right as it moves back up the branch
    def dft_post_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty")
        current = previous = self.root
        stack = []
        visited = []
        while current:
            while current.left:
                stack.append(current)
                current = current.left
            while not current.right or current.right == previous:
                visited.append(current.data)
                previous = current
                if not stack:
                    return visited
                current = stack.pop()
            stack.append(current)
            current = current.right
        return visited
    
    def dft_post_order_recursive(self):
        if not self.root:
            raise Exception("Tree is empty")
        visited = []

        def _traverse(node):
            while node:
                if node:
                    _traverse(node.left)
                    _traverse(node.right)
                    visited.append(node.data)
                return
        _traverse(self.root)
        return visited