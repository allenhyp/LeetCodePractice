from math import ceil, sqrt

class Node(object):
    def __init__(self, idx):
        self.idx = idx
        self.parent = self
        self.size = 1

    def __repr__(self):
        return "{0} ({1})\n".format(self.idx, self.size)

class Solution(object):
    def union(self, x, y):
        '''
        Function for merging 2 nodes's parents
        '''
        parentX, parentY = self.find(x), self.find(y)
        if parentX != parentY:
            parentX.parent = parentY
            parentY.size += parentX.size

    def find(self, x):
        '''
        Function for finding the parent of the node.
        '''
        if x.parent != x:
            x.parent = self.find(x.parent)
        return x.parent

    def cloudFrontCaching(self, n, edges) -> int:
        '''
        Main function for execution.
        '''
        total = 0
        nodes = [None]
        for i in range(1, n + 1):
            nodes.append(Node(i))
        for edge in edges:
            self.union(nodes[edge[0]], nodes[edge[1]])
        for i in range(1, n + 1):
            if nodes[i].parent == nodes[i]:
                total += ceil(sqrt(nodes[i].size))
        return total

def __main__():
    n = 10
    edges = [[1, 2], [1, 3], [2, 4], [3, 5], [7, 8]]
    solution = Solution()
    print(solution.cloudFrontCaching(n, edges))
    return

if __name__ == "__main__":
    __main__()
