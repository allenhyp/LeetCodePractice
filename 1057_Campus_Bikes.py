class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        for i, (w_x, w_y) in enumerate(workers):
            distances.append([])
            for j, (b_x, b_y) in enumerate(bikes):
                distances[-1].append((abs(w_x - b_x) + abs(w_y - b_y), i, j))
            distances[-1].sort(reverse=True)
        
        res = [-1] * len(workers)
        used_bikes = set()
        queue = [distances[i].pop() for i in range(len(workers))]
        heapq.heapify(queue)
        
        while len(used_bikes) < len(workers):
            (dis, worker, bike) = heapq.heappop(queue)
            if bike not in used_bikes:
                res[worker] = bike
                used_bikes.add(bike)
            else:
                heapq.heappush(queue, distances[worker].pop())
                
        return res
