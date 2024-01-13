class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node('H', 'head')
        self.tail = Node("T", 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
            
        if self.capacity == 0:
            self._remove(self.tail.prev)

        node = Node(key, value)
        self._add(node)

    def _add(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        self.map[node.key] = node
        self.capacity -= 1

    def _remove(self, node):        
        node.prev.next, node.next.prev = node.next, node.prev
        del self.map[node.key]
        self.capacity += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)