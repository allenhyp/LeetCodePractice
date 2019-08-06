class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:

    def __init__(self):
        self.root = None
        
    def traverse(self, start, end, root):
        if start >= root.end:
            if root.right:
                return self.traverse(start, end, root.right)
            else:
                root.right = Node(start, end)
                return True
        elif end <= root.start:
            if root.left:
                return self.traverse(start, end, root.left)
            else:
                root.left = Node(start, end)
                return True
        return False

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        else:
            return self.traverse(start, end, self.root)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)