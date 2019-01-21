class MaxStack:
    class Node:
        def __init__(self, val, prev, key):
            self.val = val
            self.prev = prev
            self.next = None
            self.key = key
            self.removed = False
        
        
        def __lt__(self, other):
            return self.key > other.key
    
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_length = 0
        self.stack_top = self.Node(None, None, self.stack_length)
        self.max_stack = []

        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack_length += 1
        self.stack_top.next = self.Node(x, self.stack_top, self.stack_length)
        self.stack_top = self.stack_top.next
        heapq.heappush(self.max_stack, (-x, self.stack_top))
        

    def pop(self):
        """
        :rtype: int
        """
        top_node = self.stack_top
        res = top_node.val
        if res == None:
            return None
        top_node.prev.next = None
        self.stack_top = top_node.prev
        top_node.removed = True
        del(top_node)
        return res
        

    def top(self):
        """
        :rtype: int
        """
        while self.stack_top.removed:
            self.stack_top = self.stack_top.prev
        return self.stack_top.val


    def peekMax(self):
        """
        :rtype: int
        """
        while self.max_stack[0][1].removed:
            heapq.heappop(self.max_stack)
        return -self.max_stack[0][0]
        

    def popMax(self):
        """
        :rtype: int
        """
        while self.max_stack[0][1].removed:
            heapq.heappop(self.max_stack)
        max_node = self.max_stack[0][1]
        res = max_node.val
        max_node.prev.next = max_node.next
        if max_node.next:
            max_node.next.prev = max_node.prev
        else:
            self.stack_top = max_node.prev
        max_node.removed = True
        del(max_node)
        heapq.heappop(self.max_stack)
        return res
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
