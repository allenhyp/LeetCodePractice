from typing import List
import heapq

def five_star_reviews(ratings: List[List[int]], threshold: int) -> int:
    step = 0
    pq = []
    current = 0
    n = len(ratings)
    for pos, total in ratings:
        percent = pos / total
        dif = (pos + 1) / (total + 1) - percent
        heapq.heappush(pq, (-dif, pos, total))
        current += percent

    while (current / n * 100) < threshold:
        dif, pos, total = heapq.heappop(pq)
        current += -dif
        pos, total = pos + 1, total + 1
        percent = pos / total
        dif = (pos + 1) / (total + 1) - percent
        heapq.heappush(pq, (-dif, pos, total))
        step += 1
        
    return step

if __name__ == '__main__':
    ratings = [[int(x) for x in input().split()] for _ in range(int(input()))]
    threshold = int(input())
    res = five_star_reviews(ratings, threshold)
    print(res)
