class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None


class LRUCache:        
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.length = 0
        self.capacity = capacity
        self.head = Node('H', 0)
        self.tail = Node('T', 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            self._remove(self.dic[key])
            self._add(node)
            return node.val
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            self._remove(self.dic[key])
        node = Node(key, value)
        self._add(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            node = self.tail.prev
            self._remove(node)
            del self.dic[node.key]


    def _add(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node


    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

