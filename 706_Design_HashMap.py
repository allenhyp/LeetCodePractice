class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hashTable = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size
        if self.hashTable[idx] == None:
            self.hashTable[idx] = ListNode(key, value)
        else:
            cur = self.hashTable[idx]
            while True:
                if cur.key == key:
                    cur.val = value
                    return
                elif cur.next == None:
                    cur.next = ListNode(key, value)
                    return
                else:
                    cur = cur.next

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        cur = self.hashTable[idx]
        while cur:
            if cur.key == key:
                return cur.val
            else:
                cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        pre = cur = self.hashTable[idx]
        if cur == None:
            return
        elif cur.key == key:
            self.hashTable[idx] = cur.next
            del cur
        else:
            cur = cur.next
            while cur:
                if cur.key == key:
                    pre.next = cur.next
                    del cur
                    break
                else:
                    pre, cur = pre.next, cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
