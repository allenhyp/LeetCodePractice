from collections import defaultdict
class RandomizedCollection:

    def __init__(self):
        self.elements = []
        self.map = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.elements.append(val)
        self.map[val].add(len(self.elements) - 1)
        return len(self.map[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.map or len(self.map[val]) == 0:
            return False
        
        pos = self.map[val].pop()
        if pos != len(self.elements) - 1:
            last = self.elements[-1]
            self.elements[pos] = last
            self.map[last].remove(len(self.elements) - 1)
            self.map[last].add(pos)

        self.elements.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)
        

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()