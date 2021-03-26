from typing import List
from collections import defaultdict

def shopping_patterns(products_nodes: int, products_from: List[int], products_to: List[int]) -> int:
    graph = defaultdict(set)
    for u, v in zip(products_from, products_to):
        graph[u].add(v)
        graph[v].add(u)
    res = float('inf')
    for u, ns in graph.items():
        if len(ns) < 2:
            continue
        for v in ns:
            if v > u:
                for w in ns :
                    if w > v:
                        res = min(res, sum(len(graph[x]) - 2 for x in [u, v, w]))

    return -1 if res == float('inf') else res

if __name__ == '__main__':
    products_nodes = int(input())
    products_from = [int(x) for x in input().split()]
    products_to = [int(x) for x in input().split()]
    res = shopping_patterns(products_nodes, products_from, products_to)
    print(res)
