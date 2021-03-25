from typing import List
from typing import Counter
from itertools import accumulate

import heapq

def find_profit(inventory: List[int], order: int) -> int:
    pq = [-inv for inv in inventory]
    heapq.heapify(pq)
    res = 0
    for i in range(order):
        sell = heapq.heappop(pq)
        res -= sell
        heapq.heappush(pq, sell + 1)
    return res

def seq_sum(start: int, stop: int) -> int:
    '''
    Returns sum of arithmetic sequence from start to stop (exclusive).
    sum(a, a + 1, ..., b - 1, b) = (a + b) * (b - a + 1) / 2
    '''
    return (start + stop) * (stop - start + 1) // 2

def find_profit_optimize(inventory: List[int], order: int) -> int:
    # (stock, suppliers_ount) => list of tuples
    stocks = sorted(Counter(inventory).items(), reverse=True)
    suppliers = 0
    profit = 0
    for i, (stock, extra) in enumerate(stocks):
        if order <= 0:
            break
        next_stock = stocks[i + 1][0] if i < len(stocks) - 1 else 0
        suppliers += extra
        supply = suppliers * (stock - next_stock)
        full, part = divmod(min(order, supply), suppliers)
        profit += suppliers * seq_sum(stock - full + 1, stock)\
                  + part * (stock - full)
        order -= supply
    return profit

if __name__ == '__main__':
    inventory = [int(x) for x in input().split()]
    order = int(input())
    res = find_profit(inventory, order)
    print(res)
